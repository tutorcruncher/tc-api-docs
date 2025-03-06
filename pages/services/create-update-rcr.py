import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'recipient': 2007,
    'charge_rate': 100,
    'agent': 2012,
    'agent_percentage': 10,
}
r = requests.post('https://secure.tutorcruncher.com/api/services/<id>/recipient/add/', json=data, headers=headers)
pprint.pprint(r.json())
