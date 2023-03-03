# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-11-07
#


import os
import json
import requests
from pyzentao.exceptions import InvalidJSONResponseError


def get_json(response):
    """get json from response"""

    try:
        if isinstance(response, requests.Response):
            return response.json()
        else:
            # invalid object type
            raise InvalidJSONResponseError(response)
    except json.decoder.JSONDecodeError:
        # invalid json in api response
        raise InvalidJSONResponseError(response) from None


def is_empty_dir(dir_path):
    """check out directory is empty or not"""

    return not any((True for _ in os.scandir(dir_path)))

# end
