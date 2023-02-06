import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.post('https://secure.tutorcruncher.com/api/clients/?user__first_name=Jamie/', json=data, headers=headers)
pprint.pprint(r.json())
