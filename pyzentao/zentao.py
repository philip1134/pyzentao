# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import os
import yaml
import requests
from pyzentao.attribute_dict import AttributeDict
from pyzentao.api import API
from pyzentao.session import Session
from pyzentao.response import Response
from pyzentao.common import get_json


def make_api_method(api, **kwargs):
    def _api(self, **kwargs):
        return self.request(api, **kwargs)
    return _api


class Zentao:
    """zentao main entry class"""

    def __init__(self, config):
        super(Zentao, self).__init__()

        # load config
        self._load_config(config)

        # add dynamical methods for api
        self._init_apis()

        # initialize session
        self.session = Session(
            username=self.config.username,
            password=self.config.password,
            session_api=self.apis.get("api_getSessionID"),
            login_api=self.apis.get("user_login")
        )

# public
    def request(self, api_name, **kwargs):
        """wrapper for requests.request"""

        self.session.connect()

        # check out params
        params = kwargs.pop("params", {})
        params[self.session.name] = self.session.id

        # check out request body
        data = kwargs.pop("data", {})

        # get api spec
        api = self.apis.get(api_name, kwargs)

        response = get_json(requests.request(
            method=api.get("method", "GET"),
            url=api.get("url"),
            params=params,
            data=data
        ))

        # return raw response or not
        if kwargs.pop("raw", False):
            return response
        else:
            return Response(response)

# protected
    def _init_apis(self):
        """initialize apis"""

        # load api specs
        self.apis = API(
            base_url=self.config.url,
            version=self.config.version,
            config=self.config.get("spec", None)
        )

        # generate methods by api name
        for api in self.apis.names():
            setattr(Zentao, api, make_api_method(api))

    def _load_config(self, config):
        """load configuration"""

        # load customized config
        if isinstance(config, str) and os.path.exists(config):
            # config file path
            with open(config, mode="r", encoding="utf-8") as f:
                cfg = yaml.full_load(f.read()).get("zentao")
        elif isinstance(config, dict):
            cfg = config

        self.config = AttributeDict({
            "url": "",
            "version": "15",
            "username": "",
            "password": "",
        })
        self.config.update(cfg)

        # check out url
        if not self.config.url.endswith("/"):
            self.config.url += "/"

# end
