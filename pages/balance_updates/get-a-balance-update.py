import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.get('https://secure.tutorcruncher.com/api/balance_updates/<id>/', headers=headers)
pprint.pprint(r.json())
