import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'label': 2,
}
r = requests.post('https://app.tutorcruncher.com/api/services/719520/remove_label/', json=data, headers=headers)
pprint.pprint(r.json())
