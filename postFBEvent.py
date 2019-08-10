"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""

import facebook
import requests
import sys
from os.path import dirname, join, exists,abspath
from os import environ
import datetime

sys.path.append('/home/tango/t/py34/lib/python3.4/site-packages/')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.production')

import django
django.setup()
from django.core.management import execute_from_command_line
from profiles.models import FBLocation, FBEvents


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/


tango_location = {'264587550321500':'Hyderabad', '527770257327317':'Bangalore', '1636178923304872':'Mumbai', '100006844149398':'Chennai', '197346010313291':'Auroville-Pondichery',
'305372292817505':'Pune','107857822580692' :'Mumbai Tango', '1099207956812482': 'Bangalore - Elcabeco' , '7213847061':'NewDelhi - 2 To Tango','291047664345550':'NDTS-New Delhi Tango School','1513486182213415':'Mumbai - BTangoConscious','244450719272677':'Goa Tango Community'}

#print (str(datetime.date.today()))
today = datetime.date.today()
first = today.replace(day=1)
lastmonth = first - datetime.timedelta(days=63)
sincet = lastmonth.strftime("%Y-%m-%d")
print (today)
# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join('/home/tango/t/', 'secrets.env')

if exists(env_file):
    environ.Env.read_env(str(env_file))


ACCESS_TOKEN = env('ACCESS_TOKEN')

APP_ID = env('APP_ID')
APP_SECRET = env('APP_SECRET') # DO NOT SHARE WITH ANYONE!

def get_event_for_page():
    try:
        all_events = FBEvents.objects.all()
        return all_events
    except Exception as e:
        print ('Passing to next line.Possibly because of no data returned by query', e)
        pass

def post_events(user, msg, event):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    #post  = requests.post("{}/feed?message={}".format(id, msg))
    graph.put_object(parent_object=user, connection_name='feed',
                  message=msg, link='http://thetangoindia.in/Tango-Events/')

                  

if __name__ == "__main__":
    
    e = get_event_for_page()
    event = e[0]
    picture  = e[0].Cover
    thetangoindia = 'http://thetangoindia.in/Tango-Events/'
    msg =  "New tango event in : {} {} Start Time: {} \n\nCheckout more events at:{}\n\n {} Details: {}".format(e[0].Location_Name, e[0].Place, e[0].Start_Time, thetangoindia, picture , e[0].Description)
    #post_tango_events('1743007585978030', event)
    post_events('1743007585978030', msg, event)
    #post_event_photo('1743007585978030', event, msg)
    
    
"""


class EventsForPage():
    startdate = datetime.date.today()
    enddate = startdate + datetime.timedelta(days=7)
    sdate = startdate.strftime("%Y-%m-%d %H:%M")
    edate = enddate.strftime("%Y-%m-%d %H:%M")                            
    
    def get_context_data(self, **kwargs):
        context = super(EventsForPage,self).get_context_data(**kwargs)
        context['weekback'] = FBEvents.objects.filter(Start_Time__range=[self.sdate, self.edate]).distinct()
        context['tango_location'] = tango_location
        return context
        
def post_event_photo(user, event, msg):
    graph = facebook.GraphAPI(ACCESS_TOKEN)

    graph.put_photo(image=event.Cover, album_path='1743007585978030/photos',
                  message=msg)
 
    
def post_tango_events(user, event):
    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)
    #if version 2.8 show error use 2.
    Link = str(event.Event_Link)
    attachment =  {
        'name': 'New tango event',
        'link': Link,
        'caption': 'New tango event in',
        'description': 'event.Description',
        'picture': 'event.Cover'
    }

    graph.put_wall_post(message='Upcoming Event ...', attachment=attachment, profile_id=user)"""
    