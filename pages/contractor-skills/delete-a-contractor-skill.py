import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
r = requests.delete('https://secure.tutorcruncher.com/api/contractor-skills/1/', headers=headers)
# Returns 204 on success 