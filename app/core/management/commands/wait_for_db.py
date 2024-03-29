"""
Django command to wait for database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for a database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        max_retries = 0

        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                if max_retries > 10:
                    return TimeoutError("Max retries exceeded")

                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
                max_retries += 1
        self.stdout.write(self.style.SUCCESS("Database available!"))
