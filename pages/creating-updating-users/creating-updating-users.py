import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'email': 'billy_bob@example.com',
        'last_name': 'Bob',
        'photo': 'https://picsum.photos/200/300'
        # ...
    },
    # ...
}
requests.post('...', json=data, headers=headers)
