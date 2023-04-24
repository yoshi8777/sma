import os
import json
import facebook
import requests

if __name__ == '__main__':
    token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts')

    while True:
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(posts)+"\n")

                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
