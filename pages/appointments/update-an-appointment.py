import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    "start": "2020-01-01T12:00:00Z",
    "finish": "2020-01-01T14:00:00Z",
    "topic": "Lesson 1",
    "location": None,
    "extra_attrs": {},
    "rcras": [
        {
            "recipient": 23,
            "charge_rate": "100.00"
        }
    ],
    "cjas": [
        {
            "contractor": 56,
            "pay_rate": "81.00"
        }
    ],
    "status": "planned",
    "service": 23,
}
r = requests.put('https://secure.tutorcruncher.com/api/appointment/<id>/', json=data, headers=headers)
pprint.pprint(r.json())
