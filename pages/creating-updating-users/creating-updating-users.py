import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob'
        # ...
    },
    # ...
}
requests.get('...', json=data, headers=headers)
