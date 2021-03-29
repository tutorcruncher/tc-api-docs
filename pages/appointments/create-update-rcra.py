import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "recipient": 23,
    "charge_rate": "100.00",
}
r = requests.post('https://secure.tutorcruncher.com/api/appointments/<id>/recipient/add/', json=data, headers=headers)
pprint.pprint(r.json())
