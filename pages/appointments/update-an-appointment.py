import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "start": "2020-01-01T12:00:00Z",
    "finish": "2020-01-01T14:00:00Z",
    "topic": "Lesson 1",
    "location": None,
    "extra_attrs": {},
    "status": "planned",
    "service": 23,
}
r = requests.put('https://secure.tutorcruncher.com/api/appointments/<id>/', json=data, headers=headers)
pprint.pprint(r.json())
