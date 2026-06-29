import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.get('https://app.tutorcruncher.com/api/balance-updates/', headers=headers)
pprint.pprint(r.json())
