"""
Django commands to pause execution until database is available
"""
from time import sleep

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django commands to pause execution until database is available"""

    def handle(self, *args, **options):
        """Encryption for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
