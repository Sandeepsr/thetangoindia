import sys
from os import environ
sys.path.append('/home/tango/t/py34/lib/python3.4/site-packages/')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.production')



import datetime
import pytz

utc_time = datetime.datetime.now()
print (utc_time)


#print (pytz.all_timezones)
print (pytz.common_timezones)


