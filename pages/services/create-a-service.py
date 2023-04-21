import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'allow_proposed_rates': True,
    'branch_tax_setup': None,
    'cap': None,
    'conjobs': [
        {
            'contractor': 1865741,
            'contractor_permissions': 'add-edit-complete',
            'pay_rate': 45.0
        },
        {
            'contractor': 1865742,
            'contractor_permissions': 'add-edit-complete',
            'pay_rate': 35.0
        }
    ],
    'rcrs': [
        {
            'recipient': 1865698,
            'charge_rate': 35.0
        },
        {
            'recipient': 1865702,
            'charge_rate': 25.0
        }
    ],
    'colour': 'Khaki',
    'contractor_tax_setup': None,
    'description': 'Example description for the Service which will appear on TutorCruncher',
    'dft_charge_type': 'hourly',
    'dft_charge_rate': 45.0,
    'dft_contractor_permissions': 'add-edit-complete',
    'dft_contractor_rate': 35.0,
    'dft_location': None,
    'dft_max_srs': 10,
    'extra_attrs': {'study_level': 'GCSE'},
    'extra_fee_per_apt': None,
    'inactivity_time': None,
    'name': 'Example Name',
    'net_gross': 'gross',
    'report_required': False,
    'require_rcr': False,
    'require_con_job': False,
    'review_units': 0,
    'sales_codes': None,
    'sr_premium': 0.0,
    'status': 'pending'
}
r = requests.post('https://secure.tutorcruncher.com/api/services/', json=data, headers=headers)
pprint.pprint(r.json())
