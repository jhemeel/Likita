from django.conf import settings
from base.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    username = settings.env("SUPER_USER_NAME")
    password = settings.env("SUPER_USER_PASSWORD")
    email = settings.env("SUPER_USER_EMAIL")
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username=self.username).exists():
            User.objects.create_superuser(
                username=self.username,
                email = self.email,
                password=self.password
            )
        print('Superuser has been created.')