# Chap02/twitter_get_home_timeline.py
import json
from tweepy import Cursor
from TwitterClient import get_twitter_client

if __name__ == '__main__':

    client = get_twitter_client()

    with open('home_timeline.jsonl', 'w') as f:
        for page in Cursor(client.home_timeline, count=200).pages(4):
            for status in page:
                # Process a single status
                f.write(json.dumps(status._json) + "\n")

# python TwGetHomeTimeline.py
# {"created_at": "Sun Jun 25 08:30:12 +0000 2023", "id": 1234567890123456789, "text": "This is a sample tweet.", ...}
# {"created_at": "Sun Jun 25 08:28:45 +0000 2023", "id": 1234567890123456790, "text": "Another tweet example.", ...}
# {"created_at": "Sun Jun 25 08:27:01 +0000 2023", "id": 1234567890123456791, "text": "Testing the script.", ...}
