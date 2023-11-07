"""
This file is used to create models for the core app.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# Create your models here.
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

