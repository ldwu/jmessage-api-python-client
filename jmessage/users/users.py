from jmessage import url
import json


class User(object):

    def __init__(self, jmessage):
        self.jmessage = jmessage

    @staticmethod
    def build_user(username=None, password=None, nickname=None,
                   star=None, avatar=None, gender=None, signature=None,
                   region=None, address=None, mtime=None, ctime=None):

        return dict([(key, value)
                     for key, value in locals().items() if value is not None])

    def register_user(self, users):
        users = json.dumps(users)
        register_url = url.IM_URL + url.REGIST_USER_URL
        response = self.jmessage.request("POST", users, register_url)
        return response

    def register_admin(self, admins):
        admins = json.dumps(admins)
        register_url = url.IM_URL + url.REGIST_ADMIN_URL
        response = self.jmessage.request("POST", admins, register_url)
        return response

    def get_user_by_username(self, username):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + username
        # print register_url
        body = None
        response = self.jmessage.request("GET", body, register_url)
        return response

    def put_user_password(self, username, password):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + username + "/password"
        # print register_url
        new_password = dict()
        new_password["new_password"] = password
        body = json.dumps(new_password)
        response = self.jmessage.request("PUT", body, register_url)
        return response

    def delete_user_by_username(self, username):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + username
        # print register_url
        body = None
        response = self.jmessage.request("DELETE", body, register_url)
        return response

    def blacklist_user_by_username(self, username):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + \
                       username + "/blacklist"
        # print register_url
        body = None
        response = self.jmessage.request("PUT", body, register_url)
        return response

    def delete_blacklist_by_username(self, username):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + \
                       username + "/blacklist"
        # print register_url
        body = username
        response = self.jmessage.request("DELETE", body, register_url)
        return response

    def get_blacklist(self, username):
        # print username
        register_url = url.IM_URL + url.REGIST_USER_URL + \
                       username + "/blacklist"
        # print register_url
        body = username
        response = self.jmessage.request("GET", body, register_url)
        return response

    def get_users(self, start, count):
        register_url = url.IM_URL + url.REGIST_USER_URL +\
                       "?start=" + start + "&count=" + count
        # print register_url
        body = None
        response = self.jmessage.request("GET", body, register_url)
        return response
