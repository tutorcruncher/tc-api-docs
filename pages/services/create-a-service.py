import requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'allow_proposed_rates': True,
    'branch_tax_setup': None,
    'cap': None,
    'conjobs': [
        {
            'contractor': 568503,
            'contractor_permissions': 'add-edit-complete',
            'pay_rate': 45.0,
        }
    ],
    'rcrs': [
        {
            'recipient': 562725,
            'charge_rate': 35.0,
            'agent': 885425,
            'agent_percentage': 30.0,
        }
    ],
    'colour': 'Khaki',
    'contractor_tax_setup': 8361,
    'description': 'Example description for the Service which will appear on TutorCruncher',
    'dft_charge_type': 'hourly',
    'dft_charge_rate': 45.0,
    'dft_contractor_permissions': 'add-edit-complete',
    'dft_contractor_rate': 35.0,
    'dft_location': None,
    'dft_max_srs': 10,
    'extra_attrs': {},
    'extra_fee_per_apt': None,
    'inactivity_time': None,
    'name': 'Example Name',
    'net_gross': 'gross',
    'require_rcr': True,
    'require_con_job': True,
    'review_units': 0,
    'sales_codes': None,
    'sr_premium': 0.0,
    'status': 'pending',
}
r = requests.post('https://secure.tutorcruncher.com/api/services/', json=data, headers=headers)
print(r.content.decode())
