import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'email': 'billy_bob@example.com',
    'last_name': 'Bob2',
    # ...
    'extra_attrs': {'user_dob': '1993-06-23'}
    # ...
}
r = requests.post('https://secure.tutorcruncher.com/api/contractors/', json=data, headers=headers)
pprint.pprint(r.json())

# or

r = requests.put('https://secure.tutorcruncher.com/api/contractors/<id>/', json=data, headers=headers)
pprint.pprint(r.json())
