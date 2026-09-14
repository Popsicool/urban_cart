from django.core.management.base import BaseCommand
from authentication.models import User
from django.db import transaction

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.hiit()
    def hiit(self):
        with transaction.atomic():
            User.objects.get_or_create()
        