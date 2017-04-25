import json


def get_user_id(param):
    if param.isdigit():
        param = int(param)
    else:
        with open('spotify_data.json') as data_file:
            spotify_data = json.load(data_file)

        users = spotify_data['users']
        if param in users:
            param = users[param]
        else:
            param = -1

    return param
