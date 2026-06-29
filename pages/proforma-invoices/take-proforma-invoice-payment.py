import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'amount': 100.0,
    'method': 'cash',
    'send_receipt': True,
}
r = requests.post('https://app.tutorcruncher.com/api/proforma-invoices/<id>/take_payment/', json=data, headers=headers)
pprint.pprint(r.json())
