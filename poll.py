import dnapp
from time import sleep

BASE_URL = 'https://sandboxdnac2.cisco.com/'
token = dnapp.get_token()
headers={'X-Auth-Token': '{}'.format(token)}

previous = dnapp.get_client_health()

while True:
    sleep(5)
    current = dnapp.get_client_health()
    if current != previous:
        print('Not Same.')
        current = previous
    else:
        print('Same.')