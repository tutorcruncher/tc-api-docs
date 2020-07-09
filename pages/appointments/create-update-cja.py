import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "contractor": 43,
    "charge_rate": "80.00"
}
r = requests.post('https://secure.tutorcruncher.com/api/appointment/<id>/contractor/', json=data, headers=headers)
pprint.pprint(r.json())
