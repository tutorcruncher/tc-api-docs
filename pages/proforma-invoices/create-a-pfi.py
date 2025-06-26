import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'amount': 120,
    'client': 312,
    'send_pfi': True,
    'email_pfi': False,
    'description': 'Credit Request for Billy Holiday'
}
r = requests.post('https://secure.tutorcruncher.com/api/proforma-invoices/', json=data, headers=headers)
pprint.pprint(r.json())
