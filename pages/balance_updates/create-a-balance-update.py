import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "role": 67,
    "credit_amount": 100,
    "method": "cash",
    "description": "Client paid by cash.",
    "send_receipt": True,
}
response = requests.post('https://secure.tutorcruncher.com/api/balance_updates/', json=data, headers=headers)
pprint.pprint(response.json())
