from getFBevents import get_fb_events
import sys
from config import logger, PAGE_IDS, SITE_PKG_PATH
sys.path.append(SITE_PKG_PATH)


def fb_event_cron():
    """Gets Events from facebook and run cron

    :return: list of events
    :rtype: list
    """
    try:
        return get_fb_events(PAGE_IDS)
    except Exception as err:
        logger.exception(f"Error getting FB events : {err}")


# call the cron job
fb_event_cron()
