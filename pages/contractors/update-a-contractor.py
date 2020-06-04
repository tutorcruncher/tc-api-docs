import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob2'
        # ...
    },
    # ...
}
r = requests.post('https://secure.tutorcruncher.com/api/contractors/', json=data, headers=headers)
pprint.pprint(r.json())
