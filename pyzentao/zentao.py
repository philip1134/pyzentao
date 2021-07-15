# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import yaml
import json
import urllib
import requests
from .attribute_dict import AttributeDict


class Zentao:
    """zentao main entry class"""

    def __init__(self, config):
        super(Zentao, self).__init__()

        self._load_config(config)
        self.connected = False

    def connect(self):
        """setup connection"""

        if not self.connected:
            self.connected = self._get_session() and self._login()

        return self.connected

# protected
    def _load_config(self, config):
        """load configuration"""

        if isinstance(config, str):
            # config file path
            # raise exception if config file does not exist
            with open(config, mode="r", encoding="utf-8") as f:
                cfg = yaml.full_load(f.read()).get("zentao")
        elif isinstance(config, dict):
            cfg = config

        self.config = AttributeDict({
            # zentao root url
            "root_url": "",

            # authentication
            "username": "",
            "password": "",

            # urls
            "session_url": "api-getSessionID.json",
            "login_url": "user-login.json"
        })
        self.config.update(cfg)

    def _login(self):
        """login zentao with username and password"""

        if self.session_name is None or self.session_id is None:
            return False

        resp = requests.post(
            urllib.parse.urljoin(
                self.config.root_url,
                self.config.login_url
            ),
            params={
                "account": self.config.username,
                "password": self.config.password,
                self.session_name: self.session_id
            }
        )

        self.response = resp.json()
        return "success" == self.response.get("status")

    def _get_session(self):
        """get zentao session name and session id"""

        resp = requests.get(
            urllib.parse.urljoin(
                self.config.root_url,
                self.config.session_url
            )
        )
        self.response = resp.json()

        if "success" == self.response.get("status"):
            # get data list and return to caller
            session = json.loads(self.response["data"])
            self.session_name = session["sessionName"]
            self.session_id = session["sessionID"]
            return True
        else:
            # fail to get session
            return False

# end
