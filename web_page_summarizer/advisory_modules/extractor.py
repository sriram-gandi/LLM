import requests
def request(user_input):
    response = requests.get(user_input)
    return response