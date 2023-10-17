# authy/management/commands/createsu.py
from django.conf import settings
import os, environ
from base.models import User
from django.core.management.base import BaseCommand

env = environ.Env()

class Command(BaseCommand):
    username = os.environ.get("SUPER_USER_NAME")
    password = os.environ.get("SUPER_USER_PASSWORD")
    email = os.environ.get("SUPER_USER_EMAIL")
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username=self.username).exists():
            User.objects.create_superuser(
                username=self.username,
                email = self.email,
                password=self.password
            )
        print('Superuser has been created.')