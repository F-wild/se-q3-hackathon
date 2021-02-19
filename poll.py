# import functions from dnapp.py (must be in same folder.)
import dnapp
# sleep(seconds) to force bot to wait specified time before checking
from time import sleep

# constant variables
BASE_URL = 'https://sandboxdnac2.cisco.com/'

# Acquire access token
token = dnapp.get_token()

# header field for requests
headers={'X-Auth-Token': '{}'.format(token)}

# Get initial client health info
previous = dnapp.get_client_health()

# poll dnac every 5 seconds, print whether client health is
# 'same' as last time (5 seconds ago) or 'not same'.
while True:
    sleep(5)
    current = dnapp.get_client_health()
    if current != previous:
        print('Not Same.')
        current = previous
    else:
        print('Same.')