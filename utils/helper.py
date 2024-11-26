import requests
from data import URLs
import random


def create_random_creds():
    name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(2, 8)))
    email = f"{name}@ya.ru"
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.sample(characters, random.randint(6, 10)))
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    return payload


def auth_user_and_get_creds():
    payload = create_random_creds()
    response = requests.post(f'{URLs.CREATE_USER_URL}', json=payload)
    return payload, response


def get_access_token(response):
    return response.json().get('accessToken')


if __name__ == '__main__':
    payload, response = auth_user_and_get_creds()
    print(response.status_code)
    print(payload.get('email'))
    print(payload.get('password'))
