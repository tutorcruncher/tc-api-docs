import requests

headers = {'Authorization': 'token ---API KEY---'}
r = requests.get('https://secure.tutorcruncher.com/api/qual_levels/', headers=headers)
print(r.content.decode())
