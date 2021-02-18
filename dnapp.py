import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://sandboxdnac2.cisco.com/'

# Get auth token from dnac sandbox using basic auth
def get_token():
    token = requests.post(
        BASE_URL + 'dna/system/api/v1/auth/token',
        auth = HTTPBasicAuth('devnetuser', 'Cisco123!'),
        headers={'content-type': 'application/json'},
        verify=False
    )
    data = token.json()
    return data['Token']

token = get_token()

def get_dev(device_ip):
    response = requests.get(
        BASE_URL + 'dna/intent/api/v1/network-device/ip-address/{}'.format(device_ip),
        headers={'X-Auth-Token': '{}'.format(token),
        'Content-Type': 'application/json'},
        verify=False
    )
    return response.json()
test = get_dev('10.10.20.81')
print(test)

