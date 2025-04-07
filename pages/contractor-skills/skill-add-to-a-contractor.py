import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'contractor': 69,  
    'subject': '51',  
    'qual_level': 13  
}
r = requests.post('https://secure.tutorcruncher.com/api/contractor-skills/', json=data, headers=headers)
pprint.pprint(r.json()) 