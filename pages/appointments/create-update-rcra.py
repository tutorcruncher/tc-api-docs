import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "recipient": 23,
    "charge_rate": "100.00"
}
r = requests.post('https://secure.tutorcruncher.com/api/appointment/<id>/recipient/', json=data, headers=headers)
pprint.pprint(r.json())
