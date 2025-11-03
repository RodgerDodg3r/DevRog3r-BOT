import json



def get_token():
    token = ''
    with open('./bot_auth.json', 'r') as file:
        data = json.load(file)
    token = data["token"]
    return token