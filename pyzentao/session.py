# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import json
import requests
from pyzentao.common import get_json
from pyzentao.exceptions import AuthenticationError


class Session:
    """zentao connection session"""

    def __init__(
        self,
        username,
        password,
        session_api,
        login_api,
    ):
        super(Session, self).__init__()

        self.username = username
        self.password = password
        self.session_api = session_api
        self.login_api = login_api

        self.connected = False
        self.name = None
        self.id = None

# public
    def connect(self):
        """setup connection"""

        if not self.connected:
            self.connected = self._get_session() and self._login()

        return self.connected

# protected
    def _get_session(self):
        """get zentao session name and session id"""

        response = get_json(requests.get(
            self.session_api.get("url")
        ))

        if "success" == response.get("status"):
            # get data list and return to caller
            session = json.loads(response["data"])
            self.name = session["sessionName"]
            self.id = session["sessionID"]
            return True
        else:
            # fail to get session
            raise AuthenticationError("Fail to get session")

    def _login(self):
        """login zentao with username and password"""

        response = get_json(requests.post(
            self.login_api.get("url"),
            params={
                "account": self.username,
                "password": self.password,
                self.name: self.id
            }
        ))

        if "success" == response.get("status"):
            return True
        else:
            # fail to sign in
            raise AuthenticationError(
                "Fail to sign in Zentao with account '%s', password '%s'" % (
                    self.username, self.password))


# end
