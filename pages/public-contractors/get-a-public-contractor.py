import requests

headers = {'Authorization': 'token ---API KEY---'}
r = requests.get('https://secure.tutorcruncher.com/api/public_contractors/---id---/', headers=headers)
print(r.content.decode())