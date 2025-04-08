import pprint, requests
data = {"name": "Statistic",  "category":14}
headers = {'Authorization': 'token <API KEY>'}
r = requests.post('https://secure.tutorcruncher.com/api/subjects/',json=data, headers=headers)
pprint.pprint(r.json())
