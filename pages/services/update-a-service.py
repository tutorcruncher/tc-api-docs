import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'name': 'SAT Maths with Philip',
    'dft_charge_type': 'hourly',
    'dft_charge_rate': 55,
    'dft_contractor_rate': 40,
    'status': 'pending',
    'colour': 'blue',
    'extra_attrs': {'study_level': 'A Level'}
}
r = requests.put('https://secure.tutorcruncher.com/api/services/<id>/', json=data, headers=headers)
pprint.pprint(r.json())
