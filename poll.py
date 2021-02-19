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

# Reminder how to stop process.
print('\n\n\x1b[0;30;41m' + 'Press ctrl+C (^C) to stop.' + '\x1b[0m\n\n')

# Get initial client health info
previous = dnapp.get_client_health(headers)
dnapp.format_client_health(previous)

# poll dnac every 5 seconds, print whether client health is
# 'same' as last time (30 seconds ago) or 'not same'.
def main ():
    while True:
        sleep(30)
        current = dnapp.get_client_health(headers)
        if tests(current, previous) == False:
            print('Not Same.')
            dnapp.format_client_health(current)
            current = previous
        else:
            print('Same.')

def tests(cur, pre):
    cur1 = cur['response'][0]['scoreDetail']
    pre1 = pre['response'][0]['scoreDetail']
    for i in cur1:
        if i['scoreValue'] != i['scoreValue']:
            return False

if __name__ == '__main__':
    main()