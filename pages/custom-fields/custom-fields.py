import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob2',
        # ...
        'extra_attrs': {'client_dob': '1993-06-23'},
        # ...
    },
    # ...
}
r = requests.post('https://secure.tutorcruncher.com/api/clients/', json=data, headers=headers)
pprint.pprint(r.json())
