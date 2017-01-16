import requests
from .users import User
from .messages import Message
from .groups import Group


class JMessage(object):

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.auth = (key, secret)

    def request(self, method, body, request_url, params=None):
        headers = dict()
        headers['user-agent'] = 'jpush-api-python-client'
        headers['connection'] = 'keep-alive'
        headers['content-type'] = 'application/json;charset:utf-8'
        response = self.session.request(method, request_url,
                                        data=body, params=params,
                                        headers=headers)
        return response

    def create_users(self):
        return User(self)

    def create_messages(self):
        return Message(self)

    def create_groups(self):
        return Group(self)
