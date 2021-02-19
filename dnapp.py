import requests
from requests.auth import HTTPBasicAuth
import json

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
headers={'X-Auth-Token': '{}'.format(token)}

def get_dev(device_ip):
    response = requests.get(
        BASE_URL + 'dna/intent/api/v1/network-device/ip-address/{}'.format(device_ip),
        headers={'X-Auth-Token': '{}'.format(token),
        'Content-Type': 'application/json'},
        verify=False
    )
    return response.json()
#test = get_dev('10.10.20.81')
#print(test)

def get_site_health():
    response = requests.get(
        BASE_URL + 'dna/intent/api/v1/site-health',
        headers=headers,
        verify=False
    )
    for site in response.json()['response']:
        print('Site: {0}, Health: {1}'.format(site['siteName'], site['networkHealthAverage']))
    return response.json()

#test = get_site_health()

def get_net_health():
    response = requests.get(
        BASE_URL + 'dna/intent/api/v1/network-health',
        headers=headers,
        verify=False
    )
    network_health = response.json()['response']
    print('Good: {0}, Bad: {1}, Health score: {2}'.format(network_health[0]['goodCount'], network_health[0]['badCount'], network_health[0]['healthScore']))
#test = get_net_health()

def get_client_health():
    response = requests.get(
        BASE_URL + 'dna/intent/api/v1/client-health',
        headers = headers, 
        verify = False
    )
    clients_health = response.json()
    return clients_health

#test = get_client_health()
#print(test['response'][0]['scoreDetail'])

test2 = get_client_health()['response'][0]['scoreDetail']

for i in test2:
    print(i['scoreCategory']['value'] + ': ' + str(i['scoreValue']))
    if i['scoreCategory']['value'] != "ALL":
        print("   Detail:")
        for j in i['scoreList']:
            print('   ' * 2 + 'Category ' + str(j['scoreCategory']['value']) + ': ' + str(j['clientCount']) + ' clients.')