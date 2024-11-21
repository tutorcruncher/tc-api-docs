import pprint
import requests
from urllib.parse import urlencode

headers = {'Authorization': 'token <API KEY>'}
params = {
    'distance_address': 'The Food Exchange, New Covent Garden Market, Nine Elms, London SW8 5EL, ENGLAND',
    'distance_radius': 1
}
url = f"https://secure.tutorcruncher.com/api/contractors/?{urlencode(params)}"
response = requests.get(url, headers=headers)
pprint.pprint(response.json())
