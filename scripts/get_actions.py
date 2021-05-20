import json
from pathlib import Path

import requests
import os

TC_ACTIONS_URL = 'https://secure.tutorcruncher.com/api/action-types/'


def main():
    key = os.getenv('TC_API_KEY')
    if not key:
        raise RuntimeError('No key so not building actions')
    r = requests.get(TC_ACTIONS_URL, headers={'AUTHORIZATION': 'token ' + key})
    r.raise_for_status()
    with open(Path('./data/actions.json'), 'w+') as f:
        json.dump(r.json(), f, indent=2)


if __name__ == '__main__':
    main()
