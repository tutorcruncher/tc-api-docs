import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'label': 2,
}
r = requests.post('https://secure.tutorcruncher.com/api/contractors/568433/remove-label/', json=data, headers=headers)
pprint.pprint(r.json())
