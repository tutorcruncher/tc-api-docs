import requests

headers = {'Authorization': 'token ---API KEY---'}
r = requests.get('https://secure.tutorcruncher.com/api/invoices/---id---/', headers=headers)
print(r.content.decode())
