"""
This file is used to create models for the core app.
"""
from django.conf import settings

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# Create your models here.
class UserManager(BaseUserManager):
    """This is the user manager class"""
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')

        # Create a new user model
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # Set the password
        user.set_password(password)
        # Save the user
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        # Create a new user model
        user = self.create_user(email, password)
        # Set the user as a superuser
        user.is_superuser = True
        user.is_staff = True
        # Save the user
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # is_active is a field that comes with AbstractBaseUser
    is_active = models.BooleanField(default=True)
    # is_staff is a field that comes with PermissionsMixin
    is_staff = models.BooleanField(default=False)

    # This is the model manager
    objects = UserManager()

    # This is the username field
    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        """Return the string representation of the recipe"""
        return self.title


class Tag(models.Model):
    """Tag for filtering recipes"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Return the string representation of the tag"""
        return self.name
