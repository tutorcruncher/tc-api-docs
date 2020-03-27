# This endpoint does not work!

import requests

headers = {'Authorization': 'token ---API KEY---'}
data = {
    'appointment': 11,
    'client_key': 24,
    'service_recipient_name': 'Joe Blog'
}
r = requests.post('https://secure.tutorcruncher.com/api/recipient_appointments/', json=data, headers=headers)
print(r.content.decode())
