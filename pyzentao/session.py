# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import json
import urllib
import requests


class Session:
    """zentao connection session"""

    def __init__(self, config):
        super(Session, self).__init__()

        self.config = config
        self.connected = False
        self.name = None
        self.id = None

# public
    def connect(self):
        """setup connection"""

        if not self.connected:
            self.connected = self._get_session() and self._login()

        return self.connected

    def request(self, api, **kwargs):
        """wrapper for requests.request"""

        self.connect()

        # check out par
        params = kwargs.get("params", {})
        params[self.name] = self.id

        return requests.request(
            method=self._get_method(api),
            url=self._get_url(self._get_path(api, kwargs)),
            params=params
        ).json()

# protected
    def _get_method(self, api):
        """get api method"""

        spec = self.config.api[api]
        return spec.get("method", "GET")

    def _get_url(self, path):
        """join root and path to make api url"""

        return "%s.json" % urllib.parse.urljoin(
            self.config.url, path
        )

    def _get_path(self, api, params):
        """get api path by the params according to api spec"""

        spec = self.config.api[api]
        keep = spec.get("keep", False)
        path = [spec["path"]]

        if "params" in spec and params is not None:
            for param in spec["params"]:
                if param in params:
                    path.append(str(params[param]))
                elif keep:
                    path.append("")

                print(path)

        return "-".join(path)

    def _login(self):
        """login zentao with username and password"""

        if self.name is None or self.id is None:
            return False

        resp = requests.post(
            self._get_url(self.config.api.user_login.path),
            params={
                "account": self.config.username,
                "password": self.config.password,
                self.name: self.id
            }
        )

        return "success" == resp.json().get("status")

    def _get_session(self):
        """get zentao session name and session id"""

        resp = requests.get(
            self._get_url(self.config.api.api_getSessionID.path)
        )
        response = resp.json()

        if "success" == response.get("status"):
            # get data list and return to caller
            session = json.loads(response["data"])
            self.name = session["sessionName"]
            self.id = session["sessionID"]
            return True
        else:
            # fail to get session
            return False

# end
