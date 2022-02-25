import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob'
        # ...
    },
    # ...
}
requests.post('...', json=data, headers=headers)
