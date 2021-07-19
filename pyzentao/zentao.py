# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import os
import yaml
from .attribute_dict import AttributeDict
from .session import Session


def make_api_method(api, **kwargs):
    def _api(self, **kwargs):
        return self.request(api, **kwargs)
    return _api


class Zentao:
    """zentao main entry class"""

    def __init__(self, config):
        super(Zentao, self).__init__()

        self._setup(config)

    def request(self, api, **kwargs):
        return self.session.request(api, **kwargs)

# protected
    def _setup(self, config):
        """setup zentao env"""

        self._load_config(config)
        self.session = Session(self.config)

        # add dynamical methods for api
        for api in self.config.api:
            setattr(Zentao, api, make_api_method(api))

    def _load_config(self, config):
        """load configuration"""

        # load customized config
        if isinstance(config, str):
            # config file path
            # raise exception if config file does not exist
            with open(config, mode="r", encoding="utf-8") as f:
                cfg = yaml.full_load(f.read()).get("zentao")
        elif isinstance(config, dict):
            cfg = config

        self.config = AttributeDict({
            "url": "",
            "version": "15",
            "username": "",
            "password": "",
            "api": None,
        })

        # load default api specs
        self.config.api = self._load_default_specs()
        self.config.update(cfg)

        # check out url
        if not self.config.url.endswith("/"):
            self.config.url += "/"

    def _load_default_specs(self):
        """load default api specs from yaml files"""

        specs = {}
        specs_path = os.path.join(
            os.path.dirname(__file__),
            "specs",
            "v%s" % str(self.config.version)
        )
        for file_name in os.listdir(specs_path):
            if file_name.endswith(".yml"):
                with open(os.path.join(specs_path, file_name),
                          mode="r", encoding="utf-8") as f:
                    specs.update(yaml.full_load(f.read()))

        return specs

# end
