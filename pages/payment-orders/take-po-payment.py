import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'amount': 100.0,
    'method': 'cash',
}
r = requests.post('https://secure.tutorcruncher.com/api/payment-orders/<id>/take_payment/', json=data, headers=headers)
pprint.pprint(r.json())
