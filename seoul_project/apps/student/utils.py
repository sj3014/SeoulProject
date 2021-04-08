import datetime
import jwt
from django.conf import settings


def generate_access_token(student):

    access_token_payload = {
        'uuid': student['uuid'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=15),
        'iat': datetime.datetime.utcnow(),
    }

    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(student):
    refresh_token_payload = {
        'uuid': student['uuid'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

    return refresh_token
