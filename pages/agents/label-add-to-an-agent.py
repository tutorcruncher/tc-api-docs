import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'label': 2,
}
r = requests.post('https://secure.tutorcruncher.com/api/agents/65/add-label/', json=data, headers=headers)
pprint.pprint(r.json())
