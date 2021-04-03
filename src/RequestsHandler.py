
import json
from pprint import pprint


def handle_request(request):
    with open(request) as r:
        content = json.load(r)

    data   = content['data']
    action = content['action']

    print(action, data)
