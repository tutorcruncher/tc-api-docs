import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'amount': 100.0,
    'method': 'cash',
    'send_receipt': True,
}
r = requests.post('https://secure.tutorcruncher.com/api/invoices/<id>/take_payment/', json=data, headers=headers)
print(r.content.decode())
