import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.get('https://secure.tutorcruncher.com/api/reports/', headers=headers)
pprint.pprint(r.json())
