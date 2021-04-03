
import json
from Actions import Actions


def handle_request(request):
    with open(request) as r:
        content = json.load(r)

    data   = content['data']
    action = content['action']

    if action == Actions.action_user_add:
        print(data)
    elif action == Actions.action_user_del:
        print(data)
    elif action == Actions.action_user_edit:
        print(data)
    elif action == Actions.action_vehicle_add:
        print(data)
    elif action == Actions.action_vehicle_del:
        print(data)
    elif action == Actions.action_vehicle_edit:
        print(data)
    else:
        raise Exception(f"The action '{action}' is invalid.")
