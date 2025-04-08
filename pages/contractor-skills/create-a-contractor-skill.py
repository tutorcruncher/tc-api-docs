import pprint, requests
data = {"contractor": 69,"subject": 51,"qual_level": 13}
headers = {'Authorization': 'token <API KEY>'}
r = requests.post('https://secure.tutorcruncher.com/api/contractor-skills/',json=data, headers=headers)
pprint.pprint(r.json())
