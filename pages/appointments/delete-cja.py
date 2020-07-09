import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "contractor": 43,
}
r = requests.post('https://secure.tutorcruncher.com/api/appointment/<id>/contractor/delete/', json=data, headers=headers)
pprint.pprint(r.json())
