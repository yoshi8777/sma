# Chap02/twitter_get_user_timeline.py
import sys
import json
from tweepy import Cursor
from TwitterClient import get_twitter_client


def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    client = get_twitter_client()

    fname = "user_timeline_%s.jsonl" % user
    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
            for status in page: 
                f.write(json.dumps(status._json) + "\n")



#python TwG etUserTimeline.py FaizKha25159702