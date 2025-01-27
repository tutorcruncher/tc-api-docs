import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.delete('https://secure.tutorcruncher.com/api/recipients/', headers=headers)
pprint.pprint(r.json())
