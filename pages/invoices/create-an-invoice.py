import pprint, requests

headers = {"Authorization": "token <API KEY>"}
data = {
    "appointments": [1234, 1235],
    "adhoc_charges": [567],
    "raise_behaviour": "raise-and-send",
}
r = requests.post(
    "https://secure.tutorcruncher.com/api/invoices/", json=data, headers=headers
)
pprint.pprint(r.json())
