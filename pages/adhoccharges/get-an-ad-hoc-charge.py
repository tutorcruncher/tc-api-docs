import requests

headers = {'Authorization': 'token ---API KEY---'}
r = requests.get('https://secure.tutorcruncher.com/api/adhoccharges/---id---/', headers=headers)
print(r.content.decode())
