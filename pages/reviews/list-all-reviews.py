import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.get('https://app.tutorcruncher.com/api/reviews/', headers=headers)
pprint.pprint(r.json())
