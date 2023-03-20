import os
import json
from json.decoder import JSONDecodeError

import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class BaseUtils:
    def write_api_token(self, source: str, token: str):
        data = self.read_api_token()
        data[source] = token
        with open(os.path.join(settings.BASE_DIR, 'api_token.json'), 'w') as file:
            file.write(json.dumps(data))

    @staticmethod
    def read_api_token(username: str):
        try:
            return User.objects.get(username=username).apikeys
        except ObjectDoesNotExist:
            return None


class ApiUtils:
    @staticmethod
    def send_post_request(url: str, params: dict = None, headers: dict = None):
        response = requests.post(url=url, json=params, headers=headers)
        return response.json()

    @staticmethod
    def send_get_request(url: str, params: dict = None, headers: dict = None):
        response = requests.get(url=url, json=params, headers=headers)
        return response.json()

