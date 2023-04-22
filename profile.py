import json
import os
import facebook

# $env:FACEBOOK_TEMP_TOKEN="your_access_token_here"
# Set the access token as an environment variable
token = os.environ.get('FACEBOOK_TEMP_TOKEN')

# Create a GraphAPI instance using the access token
graph = facebook.GraphAPI(token)

# Use the GraphAPI to retrieve the user's name and location
profile = graph.get_object('me', fields='name,location')

# Print the profile information in a formatted JSON string
print(json.dumps(profile, indent=4))
