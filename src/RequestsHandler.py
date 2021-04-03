
import json


def handle_request(request):
    with open(request) as r:
        content = json.load(r)
        print(content.get('data'))
