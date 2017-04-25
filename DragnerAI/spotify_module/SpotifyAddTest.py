import json

with open('spotify_data.json') as data_file:
    spotify_data = json.load(data_file)

users = spotify_data['users']

if 'mcq2' in users:
    print('dupa')
else:
    print('mcq')
#
# def get_user_id(self, param):
#     if not param.isdigit():
