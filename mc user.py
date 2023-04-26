import requests
import time

# list of usernames to check
usernames = ['example1', 'example2', 'example3']

# Epic Games API endpoint for checking username availability
url = 'https://accounts.launcher-website-prod07.ol.epicgames.com/account/api/public/account'

# headers to simulate a valid user agent and prevent errors from Epic's server
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# loop through the list of usernames and check for availability
for username in usernames:
    payload = {'name': username}
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()['status']

    # check if the username is available
    if result == 'UNAVAILABLE':
        print(f"{username} is not available.")
    else:
        print(f"{username} is available!")
    
    # wait 0.5 seconds to avoid overloading Epic's server
    time.sleep(0.5)
