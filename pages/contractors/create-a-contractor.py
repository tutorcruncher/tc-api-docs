import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'user': {
        'first_name': 'Billy',
        'last_name': 'Bob',
        'email': 'billy_bob@example.com',
        'mobile': '07123456789',
        'phone': '02081234567',
        'street': '177 South Lambeth Road',
        'state': None,
        'town': 'London',
        'country': 183,
        'postcode': 'SW8 1XP',
        'latitude': '51.5549',
        'longitude': '-0.1084',
        'timezone': 'Europe/London',
    },
    'status': 'live',
    'change_via_branch': True,
    'default_rate': 80.0,
    'receive_service_notifications': True,
    'calendar_colour': 'LimeGreen',
    'extra_attrs': {},
}
r = requests.post('https://secure.tutorcruncher.com/api/contractors/', json=data, headers=headers)
print(r.content.decode())
