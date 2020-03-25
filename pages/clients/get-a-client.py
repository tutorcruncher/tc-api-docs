import requests

headers = {'Authorization': 'token ---API KEY---'}
r = requests.get('https://secure.tutorcruncher.com/api/clients/---id---/', headers=headers)
print(r.content.decode())
