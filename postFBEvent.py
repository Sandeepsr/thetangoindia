"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""

# from django.core.management import execute_from_command_line
import facebook
import sys
from os.path import dirname, join, exists, abspath
from os import environ
import environ
import datetime
from config_settings import logger, SITE_PKG_PATH, PROJECT_BASE_DIR  # TANGO_LOCATION
sys.path.append(SITE_PKG_PATH)
environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.production')

# import after sys. path append
import django
django.setup()
from profiles.models import FBEvents  # FBLocation,

# Use 12factor inspired environment variables or from a file
env = environ.Env()

# print (str(datetime.date.today()))
today = datetime.date.today()
first = today.replace(day=1)
lastmonth = first - datetime.timedelta(days=63)
sincet = lastmonth.strftime("%Y-%m-%d")
logger.info("Date today: {}".format(today))


# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(PROJECT_BASE_DIR, 't', 'secrets.env')

if exists(env_file):
    environ.Env.read_env(str(env_file))


ACCESS_TOKEN = env('ACCESS_TOKEN')

APP_ID = env('APP_ID')
APP_SECRET = env('APP_SECRET')  # DO NOT SHARE WITH ANYONE!


def get_event_for_page():
    try:
        all_events = FBEvents.objects.all()
        return all_events
    except Exception as e:
        logger.exception(
            f'Passing to next line.Possibly because of no data returned by query: {e}')


def post_events(user, msg, event):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    # post  = requests.post("{}/feed?message={}".format(id, msg))
    graph.put_object(parent_object=user, connection_name='feed',
                     message=msg, link='http://thetangoindia.in/Tango-Events/')


if __name__ == "__main__":

    e = get_event_for_page()
    event = e[0]
    picture = e[0].Cover
    thetangoindia = 'http://thetangoindia.in/Tango-Events/'
    msg = "New tango event at : {} {} Start Time: {} \n\nCheckout more events at:{}\n\n {} Details: {}".format(e[0].Location_Name,
                                                                                                               e[0].Place, e[0].Start_Time, thetangoindia,
                                                                                                               picture, e[0].Description)
    # post_tango_events('1743007585978030', event)
    post_events('1743007585978030', msg, event)
    # post_event_photo('1743007585978030', event, msg)


"""
class EventsForPage():
    startdate = datetime.date.today()
    enddate = startdate + datetime.timedelta(days=7)
    sdate = startdate.strftime("%Y-%m-%d %H:%M")
    edate = enddate.strftime("%Y-%m-%d %H:%M")                            
    
    def get_context_data(self, **kwargs):
        context = super(EventsForPage,self).get_context_data(**kwargs)
        context['weekback'] = FBEvents.objects.filter(Start_Time__range=[self.sdate, self.edate]).distinct()
        context['tango_location'] = TANGO_LOCATION
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

    graph.put_wall_post(message='Upcoming Event ...', attachment=attachment, profile_id=user)
    """
