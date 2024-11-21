import pprint
import requests

headers = {'Authorization': 'token <API KEY>'}
url = 'https://secure.tutorcruncher.com/api/contractors/'

response = requests.get(url, headers=headers)
data = response.json()
pprint.pprint(data['results'])

while data.get('next_page'):
    url = data['next_page']
    response = requests.get(url, headers=headers)
    data = response.json()
    pprint.pprint(data['results'])
