from jmessage import url
import json


class Group(object):

    def __init__(self, jmessage):
        self.jmessage = jmessage

    @staticmethod
    def build_group(owner_username=None, name=None,
                    members_username=None, desc=None):
        return dict([(key, value)
                     for key, value in locals().items() if value is not None])

    def create_group(self, group):
        group_url = url.IM_URL + url.GROUPS_URL
        body = json.dumps(group)
        response = self.jmessage.request("POST", body, group_url)
        return response

    def get_group(self, gid):
        group_url = url.IM_URL + url.GROUPS_URL + gid
        body = None
        response = self.jmessage.request("GET", body, group_url)
        return response

    def put_group(self, gid, group):
        group_url = url.IM_URL + url.GROUPS_URL + gid
        body = json.dumps(group)
        response = self.jmessage.request("PUT", body, group_url)
        return response

    def delete_group(self, gid):
        group_url = url.IM_URL+url.GROUPS_URL + gid
        body = None
        response = self.jmessage.request("DELETE", body, group_url)
        return response

    def put_group_members(self, gid, add, remove=None):
        group_url = url.IM_URL + url.GROUPS_URL + gid + "/members"
        members = dict()
        members["add"] = add
        body = json.dumps(members)
        response = self.jmessage.request("POST", body, group_url)
        return response

    def get_group_members(self, gid):
        group_url = url.IM_URL + url.GROUPS_URL + gid + "/members"
        body = None
        response = self.jmessage.request("GET", body, group_url)
        return response

    def get_groups_by_username(self, username):
        # print username
        group_url = url.IM_URL + url.REGIST_USER_URL + username + "/groups/"
        # print group_url
        body = None
        response = self.jmessage.request("GET", body, group_url)
        return response

    def get_groups_list(self, start, count):
        group_url = url.IM_URL + url.GROUPS_URL
        # print group_url
        body = None
        response = self.jmessage.request(
            "GET",
            body,
            group_url,
            params=dict(start=start, count=count))

        return response

