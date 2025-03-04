import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.post('https://secure.tutorcruncher.com/api/tenders/<id>/accept/', headers=headers)
pprint.pprint(r.json())
