import pprint, requests

headers = {'Authorization': 'token <API KEY>'}

# Get all appointments
r = requests.get('https://secure.tutorcruncher.com/api/appointments/', headers=headers)
pprint.pprint(r.json())

# Filter by client ID
r = requests.get('https://secure.tutorcruncher.com/api/appointments/?client=123', headers=headers)
pprint.pprint(r.json())

# Filter by status
r = requests.get('https://secure.tutorcruncher.com/api/appointments/?status=planned', headers=headers)
pprint.pprint(r.json())

# Filter by both client and status
r = requests.get('https://secure.tutorcruncher.com/api/appointments/?client=123&status=complete', headers=headers)
pprint.pprint(r.json())
