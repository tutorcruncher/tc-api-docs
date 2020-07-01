import pprint, requests

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
    'commission_rate': 10.1,
    'calendar_colour': 'LimeGreen',
    'extra_attrs': {},
    'send_emails': True,
}
r = requests.post('https://secure.tutorcruncher.com/api/agents/', json=data, headers=headers)
pprint.pprint(r.json())
