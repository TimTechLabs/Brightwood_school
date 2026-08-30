import os
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds demo user credentials and loads student fixtures'

    def handle(self, *args, **kwargs):
        # 1. Create Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Successfully created demo superuser!'))

        # 2. Locate and load students.json
        json_path = os.path.join(settings.BASE_DIR, 'students.json')
        
        if os.path.exists(json_path):
            call_command('loaddata', json_path)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded fixture from {json_path}!'))
        else:
            self.stdout.write(self.style.ERROR(f'Fixture file not found at {json_path}'))