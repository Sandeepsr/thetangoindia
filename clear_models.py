import sys
sys.path.append('/home/tango/t/py34/lib/python3.4/site-packages/')
sys.path.append('/home/tango/t/tango/src/profiles/')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.development')

import django
django.setup()
from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand
from models import Tango_Location, Tango_Events


class Command(BaseCommand):
    def handle(self, *args, **options):
        Tango_Location.objects.all().delete
        Tango_Events.objects.all().delete()
