"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""

import facebook
import requests
from config_settings import SITE_PKG_PATH, PROJECT_BASE_DIR, logger, TANGO_LOCATION
import sys
import os
from os.path import join, exists
import datetime
from os import environ
import environ

sys.path.append(SITE_PKG_PATH)
environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings.production')

import django
django.setup()
from profiles.models import FBLocation, FBEvents


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/

# print(str(datetime.date.today()))
today = datetime.date.today()
first = today.replace(day=1)
lastmonth = first - datetime.timedelta(days=33)
sincet = lastmonth.strftime("%Y-%m-%d")
logger.info("Stat date of script: {}".format(today))

# Use 12factor inspired environment variables or from a file
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
ENV_FILE = join(os.path.join(PROJECT_BASE_DIR, 't', 'secrets.env'))

if exists(ENV_FILE):
    logger.error("Found the env file")
    environ.Env.read_env(str(ENV_FILE))
else:
    logger.error("Failed to find the env file")

ACCESS_TOKEN = env('ACCESS_TOKEN')

P_ACCESS_TOKEN_THETI = env('P_ACCESS_TOKEN_THETI')

P_ACCESS_TOKEN_TIIN = env('P_ACCESS_TOKEN_TIIN')

APP_ID = env('APP_ID')
APP_SECRET = env('APP_SECRET')  # DO NOT SHARE WITH ANYONE!


def user_friendly_time(time_str):
    try:
        uf_time = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S%z')
        format = "%a %b %d %H:%M:%S %Y"
        return uf_time.strftime(format)
    except Exception as err:
        logger.exception("Could not convert to user_friendly_time {}".format(err))
        return time_str


def get_events(user):
    try:
        events = list()
        logger.info("Getting events from grpah api...")
        graph = facebook.GraphAPI(ACCESS_TOKEN)
        profile = graph.get_object(user)
        posts = graph.get_connections(profile['id'], 'events', fields='id,attending_count,\
        cover,description,end_time,start_time,name,\
        place,updated_time', since=sincet)
        # print(posts)
        while True:
            try:
                # Perform some action on each post in the collection we receive from
                # Facebook.
                for post in posts['data']:
                    events.append(post)
                # Attempt to make a request to the next page of data, if it exists.
                posts = requests.get(posts['paging']['next']).json()
            except KeyError:
                # When there are no more pages (['paging']['next']), break from the
                # loop and end the script.
                break
        return events
    except Exception as e:
        logger.exception("Failure getting event data : {}".format(e))


def get_existing_events():
    dpost_id = list()
    try:
        dist_id = FBLocation.objects.all()
        for i in dist_id:
            dpost_id.append(i.Name)
        return dpost_id
    except Exception as e:
        logger.exception(
            'Passing to next item. Possibly because of no data returned by query: {}'.format(e))


def get_existing_event_ids():
    e_id = list()
    try:
        dist_id = FBEvents.objects.all()
        for i in dist_id:
            e_id.append(i.Event_Id)
        return e_id
    except Exception as e:
        logger.exception(
            'Passing to next item. Possibly because of no data returned by query: {}'.format(e))


def delete_event(Event_Id):
    try:
        FBEvents.objects.filter(Event_Id=Event_Id).delete()
    except Exception as e:
        logger.exception(
            'delete_event: Passing to next line. Possibly because of no data returned by query: {}'.format(e))


def post_events(location_name, post_name, picture, description, start_time, end_time, event_link, place):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    graph_tiin = facebook.GraphAPI(P_ACCESS_TOKEN_TIIN)
    thetangoindia_fb_grp = "1743007585978030"  # thetangoindia FB group
    # thetangoindia_fb_page = "334065376933472" #thetangoindia FB Page
    # tangoinindia = "1542666775825337"
    tango_in_india = "428875644194564"
    thetangoindia = 'http://thetangoindia.in/Tango-Events/'
    uf_start_time = user_friendly_time(start_time)
    msg = "{} - {} {} \nStart Time: {} \n\nVisit {} to see events across India.\n\n Details: {}".format(post_name,
                                                                                                        location_name,
                                                                                                        place,
                                                                                                        uf_start_time,
                                                                                                        thetangoindia,
                                                                                                        description)
    # post  = requests.post("{}/feed?message={}".format(id, msg))

    try:
        graph_tiin.put_object(parent_object=tango_in_india,
                              connection_name='feed', message=msg, link=event_link)
        logger.warning("Posted a new event in tango_in_india: {}".format(event_link))
    except Exception as e:
        logger.exception(
            "Exception while posting new event to tango_in_india FB page: {}, {}, {}".format(location_name, event_link, e))

    try:
        graph.put_object(parent_object=thetangoindia_fb_grp,
                         connection_name='feed', message=msg, link=event_link)
        logger.warning(
            "Posted a new event in tango_in_india_fb_group: {}".format(event_link))
    except Exception as e:
        logger.exception(
            "Exception while posting new event to thetangoindia_fb_grp: {}, {}, {}".format(location_name, event_link, e))


def add_event_helper(pageid, events, e_id, location_get, d_loc=None, loc_name=None):

    for event in events:
        loc = location_get
        location_name = 'https://www.facebook.com/events/{}'.format(
            event["id"]) if not loc_name else loc_name
        updated_time = event["updated_time"]
        post_name = 'Tango Event' if 'name' not in event.keys(
        ) else event["name"]
        picture = 'NA' if "cover" not in event.keys(
        ) else event["cover"]["source"]
        post_id = event["id"]
        description = 'Tango' if 'description' not in event.keys(
        ) else event["description"]
        # attending_count=event["attending_count"]
        start_time = event["start_time"]
        end_time = event["start_time"] if 'end_time' not in event.keys(
        ) else event["end_time"]
        event_link = 'https://www.facebook.com/events/{}'.format(
            event["id"]) if "event_link" not in event.keys() else event["id"]
        place = ' Check description for details..' if 'place' not in event.keys(
        ) else '# {}'.format(event["place"]["name"])

        if event["id"] in e_id:
            logger.warning('Duplicate Event..deleting and re-addding {}, {}, {}'.format(
                location_name, start_time, event["id"]))
            delete_event(event["id"])
            add_event(loc=loc, location_name=place, updated_time=updated_time, post_name=post_name,
                      picture=picture, post_id=post_id,
                      description=description, start_time=start_time, end_time=end_time,
                      event_link=event_link, place=place)
            # if event["id"]  == '2324579304275132' or event['id'] == '920226871646597':
            # post_events(location_name=location_name,post_name=post_name,picture=picture,description=description,
            # start_time=start_time,end_time=end_time,event_link=event_link,place=place)
            # sys.exit()
        else:
            logger.info('New Event... NOT Duplicate..Event..added.. {}, {}, {}'.format(
                location_name, start_time, event["id"]))
            # TODO: changed location_name due to some bug
            add_event(loc=loc, location_name=place, updated_time=updated_time, post_name=post_name,
                      picture=picture, post_id=post_id,
                      description=description, start_time=start_time, end_time=end_time,
                      event_link=event_link, place=place)
            post_events(location_name=place, post_name=post_name, picture=picture,
                        description=description,
                        start_time=start_time, end_time=end_time, event_link=event_link, place=place)


def populate(pageid, events, d_loc, e_id):
    if pageid in d_loc:
        location_get = get_location(pageid)
        loc_name = str(TANGO_LOCATION[pageid])
        add_event_helper(pageid, events, e_id, location_get,
                         d_loc=d_loc, loc_name=loc_name)

    else:
        location_add = add_location(pageid)
        loc_id = str(location_add.Name)
        loc_id_name = str(TANGO_LOCATION[loc_id])
        add_event_helper(pageid, events, e_id, location_get,
                         d_loc=loc_id, loc_name=loc_id_name)


def add_event(loc, location_name, updated_time, post_name, picture, post_id, description, start_time, end_time,
              event_link, place):
    p = FBEvents.objects.update_or_create(Location=loc, Location_Name=location_name, Updated_Time=updated_time,
                                          Event_Name=post_name, Cover=picture,
                                          Event_Id=post_id, Description=description, Start_Time=start_time,
                                          End_Time=end_time, Event_Link=event_link, Place=place)[0]
    p.Location = loc
    p.Location_Name = location_name
    p.Start_Time = start_time
    p.Updated_Time = updated_time
    p.End_Time = end_time
    p.Event_Name = post_name
    p.Cover = picture
    p.Event_Id = post_id
    p.Description = description
    p.Event_Link = event_link
    p.Place = place
    p.save()
    return p


def add_location(name):
    c = FBLocation.objects.update_or_create(Name=name)[0]
    return c


def get_location(name):
    try:
        c = FBLocation.objects.get(Name=name)
        return c
    except Exception as e:
        logger.warning(
            'Adding this new location {} as no data returned by query: {}'.format(name, e))
        return add_location(name)


def get_fb_events(pageids):
    logger.warning("Starting Tango event gathering script...")
    for pageid in pageids:
        events = get_events(pageid)
        if events:
            try:
                d_loc = get_existing_events()
            except Exception as e:
                logger.warning(
                    'Passing to next event. Possibly because of no data returned by query: {}'.format(e))
            try:
                e_id = get_existing_event_ids()
            except Exception as e:
                logger.warning(
                    'Passing to next event. Possibly because of no data returned by query: {}'.format(e))
            populate(pageid, events, d_loc, e_id)
        else:
            logger.error("Got empty events list from facebook graph api")
    logger.warning('Done running Tango event gathering script...')
