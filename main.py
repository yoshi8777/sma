import requests

# Set the access token obtained from the OAuth flow
access_token = "EAACtKlcIphcBAHZBUegW4mWfP2nAWEdkcg0ru09IArLSt5LyHuAdRKRAgYZCyGvG" \
               "qcJ2tBgO5AvLSy1sZCjZBT1Hv6WfqDpOJZAvhAp" \
               "fuEoOeW9f1ZCcEETwOczt3R" \
               "9nJbgCeNHZARcsEmiVLBVlILINNi1hHG5uu7yGrUamNcZCkHnKoaftpM7blhXo29vel7rjZCw74j8hZA6QXyDFmb" \
               "MUGs2HG9SlJj9OF53MX5N3UVqu8agN8baaPVwEYxvm3y0zAZD"

# Make an API request to retrieve the user's basic information
response = requests.get(f"https://graph.facebook.com/me?access_token={access_token}")
user_data = response.json()

# Print the user's username
print("Username:", user_data["name"])

# Make an API request to retrieve the user's friend requests
response = requests.get(f"https://graph.facebook.com/me/friendrequests?access_token={access_token}")
friend_requests = response.json()

# Check if the "data" key exists in the friend_requests dictionary
if "data" in friend_requests:
    # Print the number of friend requests
    print("Friend requests:", len(friend_requests["data"]))
else:
    print("No friend requests found.")
