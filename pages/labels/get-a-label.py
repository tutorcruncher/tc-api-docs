import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.get('https://app.tutorcruncher.com/api/labels/<id>/', headers=headers)
pprint.pprint(r.json())
