import sys
from config_settings import logger, PAGE_IDS, SITE_PKG_PATH
sys.path.append(SITE_PKG_PATH)
# below import needed after append
from getFBevents import get_fb_events


def fb_event_cron():
    """Gets Events from facebook and run cron

    :return: list of events
    :rtype: list
    """
    try:
        return get_fb_events(PAGE_IDS)
    except Exception as err:
        logger.exception("Error getting FB events :{}".format(err))


# call the cron job
fb_event_cron()
