import requests

headers = {'Authorization': 'token <API KEY>'}

data = {
  "id": 568433,
  "email": "billy_bob@example.com",
  "last_name": "Bob",
  "mobile": "07842 485 204",
  "photo": "https://photo_url.com/200/300"
   # ...
}

requests.post('...', json=data, headers=headers)
