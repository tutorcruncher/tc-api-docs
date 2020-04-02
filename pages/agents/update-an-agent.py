import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob2'
        # ...
    },
    # ...
}
r = requests.post('https://secure.tutorcruncher.com/api/agents/', json=data, headers=headers)
print(r.content.decode())
