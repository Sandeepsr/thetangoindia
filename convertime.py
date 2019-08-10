import pytz
import datetime
import sys
from os import environ
from config_settings import PROJECT_BASE_DIR, PROJECT_DIR, SITE_PKG_PATH
sys.path.append(SITE_PKG_PATH)

environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.production')


utc_time = datetime.datetime.now()
# print (pytz.all_timezones)
# print (pytz.common_timezones)
