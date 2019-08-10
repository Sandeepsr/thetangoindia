import requests
import sys
from config_settings import logger


# See http://www.unixtimestamp.com/ to generate Unix timestamps online
PAYLOAD = {
    'until': 1511624381,  # Unix timestamps
    'since': 1511609400,  # Unix timestamps
    'limit': 25,  # number of posts
    'access_token': '',  # your access token
}

BASE_API = 'https://graph.facebook.com'

POST_ENDPOINT = BASE_API + \
    '/me/?fields=feed.with(replae with unique text in post to filter)'

POST_RESPONSE = requests.get(POST_ENDPOINT, params=PAYLOAD)

if POST_RESPONSE.status_code != requests.codes.ok:
    error = POST_RESPONSE.json()['error']['message']
    logger.error(f'Error: {error}')
    sys.exit(0)

posts_dict = POST_RESPONSE.json()["feed"]['data']
logger.info(f'Post dict: {posts_dict}')

logger.info("Total posts to delete: %d" % len(posts_dict))
for post in posts_dict:
    logger.warning("Deleting [%s] " % (post['id']))
    requests.delete(BASE_API + '/' + post['id'], params=PAYLOAD)
    logger.warning("Deleted [%s] \n" % (post['id']))
