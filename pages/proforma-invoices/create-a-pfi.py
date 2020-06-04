import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
client_id = 123
data = {
    'amount': 120,
    'client': client_id,
    'send_pfi': True,
}
r = requests.post('https://secure.tutorcruncher.com/api/clients/', json=data, headers=headers)
pprint.pprint(r.json())
