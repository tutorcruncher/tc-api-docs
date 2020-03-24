import requests

headers = {'Authorization': 'token fbbc2a6f0f56962239e6c21b81183b02972c441a'}
r = requests.get('https://secure.tutorcruncher.com/api/appointments/<id>/', headers=headers)
print(r.content.decode())
