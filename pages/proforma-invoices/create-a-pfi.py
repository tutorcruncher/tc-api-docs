import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'amount': 120,
    'client': 312,
    'raise_behaviour': 'raise-and-send',
    'description': 'Credit Request for Billy Holiday'
}
r = requests.post('https://secure.tutorcruncher.com/api/proforma-invoices/', json=data, headers=headers)
pprint.pprint(r.json())
