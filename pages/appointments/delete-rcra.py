import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "recipient": 23,
}
r = requests.post('https://secure.tutorcruncher.com/api/appointment/<id>/recipient/delete/', json=data, headers=headers)
pprint.pprint(r.json())
