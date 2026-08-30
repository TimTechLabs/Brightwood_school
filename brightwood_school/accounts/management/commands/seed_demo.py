from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds demo user credentials and loads student fixtures'

    def handle(self, *args, **kwargs):
        # 1. Create Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Successfully created demo superuser!'))

        # 2. Load all students from JSON file
        if os.path.exists('students.json'):
            call_command('loaddata', 'students.json')
            self.stdout.write(self.style.SUCCESS('Successfully loaded all student records!'))
        else:
            self.stdout.write('students.json file not found.')