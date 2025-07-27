import jwt
import datetime
import json


def generate_token(req_username, req_password, secret_key):

    with open('config.json', 'r') as f:
        data = json.load(f)

        username = data['Credentials']['username']
        password = data['Credentials']['password']
        secret_key = data['Credentials']['secret_key']
        token_timespan = data['Credentials']['token_timeSpan']

    if username == req_username and password == req_password and secret_key == secret_key:
        payload = {
            "username": req_username,
            "password": req_password,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=token_timespan)
        }
        return jwt.encode(payload, secret_key, algorithm="HS256")
    else:
        return "Invalid Credentials"

def validate_token(token_value):

    with open('config.json', 'r') as f:
        data = json.load(f)
        secret_key = data['Credentials']['secret_key']

    try:
        jwt.decode(token_value, secret_key, algorithms=["HS256"])
        return "Valid"
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"