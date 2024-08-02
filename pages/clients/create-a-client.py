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
    'status': 'live',
    'is_taxable': False,
    'received_notifications': [
        'invoice_reminders',
        'invoices',
        'apt_reminders',
        'pfi_reminders',
        'credit-requests',
        'low_balance_reminders',
        'broadcasts'
    ],
    'change_via_branch': True,
    'auto_charge': 0,
    'associated_admin': 12,
    'associated_agent': 34,
    'calendar_colour': 'LimeGreen',
    'extra_attrs': {'client_dob': '1993-06-23'},
    'send_emails': True,
}
r = requests.post('https://secure.tutorcruncher.com/api/clients/', json=data, headers=headers)
pprint.pprint(r.json())
