import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "contractor": 43,
    "pay_rate": "100.00",
    "contractor_permissions": "edit"
}
r = requests.post('https://secure.tutorcruncher.com/api/services/<id>/contractor/add/', json=data, headers=headers)
pprint.pprint(r.json())
