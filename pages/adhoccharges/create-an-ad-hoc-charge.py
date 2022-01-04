import pprint, requests, datetime

headers = {'Authorization': 'token <API KEY>'}
data = {
    'service': 26,
    'client': 37,
    'charge_client': 25,
    'category': 7,
    'date_occurred': datetime.datetime(2021, 1, 1),
    'description': 'Registration fee'
}
r = requests.post('https://secure.tutorcruncher.com/api/adhoccharges/', data=data, headers=headers)
pprint.pprint(r.json())
