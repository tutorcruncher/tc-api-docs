import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "contractor": 43,
    "pay_rate": "80.00"
}
r = requests.post('https://secure.tutorcruncher.com/api/appointments/<id>/contractor/add/', json=data, headers=headers)
pprint.pprint(r.json())
