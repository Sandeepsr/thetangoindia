import requests
import pprint
import sys

# See http://www.unixtimestamp.com/ to generate Unix timestamps online
payload = {
            'until': 1511624381, # Unix timestamps
            'since': 1511609400, # Unix timestamps
            'limit': 25, # number of posts
            'access_token': '', # your access token
        }

base_api = 'https://graph.facebook.com'

posts_endpoint = base_api + '/me/?fields=feed.with(replae with unique text in post to filter)'

posts_response = requests.get(posts_endpoint, params=payload)

if posts_response.status_code != requests.codes.ok:
    print('Error: ' + posts_response.json()['error']['message'])
    sys.exit(0)

posts_dict = posts_response.json()["feed"]['data']
#pprint.pprint(posts_dict)

print("Total posts to delete: %d" % len(posts_dict))
for post in posts_dict:
    print("Deleting [%s] " % (post['id']))
    requests.delete(base_api + '/' + post['id'], params=payload)
    print("Deleted [%s] \n" % (post['id']))