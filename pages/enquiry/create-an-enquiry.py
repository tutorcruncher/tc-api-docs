import requests

headers = {'Authorization': 'token ---API KEY---'}
data = {
    'client_name': 'Joe Blog',
    'client_email': 'joe_blog@example.com',
    'client_phone': '07123456789',
    'service_recipient_name': 'Billy Blog',
    'attributes': {
        'custom-field-1': 'Some text can go here',
    },
    'contractor': 568503,
    'subject': 16384,
    'qual_level': 109721,
    'terms_and_conditions': True,
}
r = requests.post('https://secure.tutorcruncher.com/api/enquiry/', json=data, headers=headers)
print(r.content.decode())
