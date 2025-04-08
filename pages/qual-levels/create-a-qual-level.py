import pprint, requests
data = {"name": "A Level",  "ranking":2}
headers = {'Authorization': 'token <API KEY>'}
r = requests.post('https://secure.tutorcruncher.com/api/qual_levels/',json=data, headers=headers)
pprint.pprint(r.json())
