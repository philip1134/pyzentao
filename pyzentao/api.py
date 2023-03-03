# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-19
#


import os
import yaml
import urllib
from pyzentao.utils import is_empty_dir
from pyzentao.exceptions import APINameError, APISpecNotFoundError


class API:
    """zentao api collection"""

    def __init__(
        self,
        base_url,
        spec=None
    ):
        super(API, self).__init__()

        self.base_url = base_url
        self._load(spec)

# public
    def get(self, name, params=None):
        """get api config by api name"""

        spec = self._specs.get(name, None)
        if spec is None:
            raise APINameError(name)

        spec["url"] = self._get_url(name, params)
        return spec

    def names(self):
        """wrapper for get data keys"""

        return self._specs.keys()

# protected
    def _get_url(self, name, params):
        """join root and path to make api url"""

        # combine path by spec and params
        spec = self._specs.get(name)
        paths = [spec["path"]]

        if "params" in spec and isinstance(params, dict):
            # placeholder for parameter
            keep = spec.get("keep", False) or params.pop("keep", False)

            for param in spec["params"]:
                if param in params:
                    paths.append(str(params[param]))
                elif keep:
                    paths.append("")

        return "%s.json" % urllib.parse.urljoin(
            self.base_url, "-".join(paths)
        )

    def _load(self, path):
        """load spec from the specified path"""

        self._specs = {}

        # check out spec path
        if path is None or \
           not os.path.exists(path) or \
           (os.path.isdir(path) and is_empty_dir(path)):
            raise APISpecNotFoundError(path)

        if os.path.isdir(path):
            # path is a directory
            for file_name in os.listdir(path):
                self._load_file(os.path.join(path, file_name))
        else:
            # path is a file
            self._load_file(path)

    def _load_file(self, path):
        """load spec from the specified file path"""

        if os.path.exists(path) and path.endswith(".yml"):
            with open(path, mode="r", encoding="utf-8") as f:
                self._specs.update(yaml.full_load(f.read()))


# end
