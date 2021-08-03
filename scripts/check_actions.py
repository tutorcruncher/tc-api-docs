import json
import os
from pathlib import Path

import requests

TC_ACTIONS_URL = 'https://secure.tutorcruncher.com/api/action-types/'


def main():
    key = os.getenv('TC_API_KEY')
    if not key:
        raise RuntimeError('No key so not building actions')
    r = requests.get(TC_ACTIONS_URL, headers={'AUTHORIZATION': 'token ' + key})
    r.raise_for_status()
    with open(Path('./data/actions.json'), 'r') as f:
        file_json = json.load(f)
        assert r.json() == file_json, 'actions.json needs updating, please run "get_actions.py" to update.'


if __name__ == '__main__':
    main()
