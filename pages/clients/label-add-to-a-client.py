import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'label': 2,
}
r = requests.post('https://secure.tutorcruncher.com/api/clients/3/add-label/', json=data, headers=headers)
pprint.pprint(r.json())
