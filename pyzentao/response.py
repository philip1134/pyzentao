# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import json
import requests
from .attribute_dict import AttributeDict


class Response:
    """zentao api response"""

    def __init__(self, raw):
        super(Response, self).__init__()

        self.raw = raw
        self.status = None
        self.data = {}

        self.parse()

# public
    def parse(self):
        """setup connection"""

        if isinstance(self.raw, dict):
            self.status = self.raw.get("status", None)
            self.data = AttributeDict(
                json.loads(self.raw.get("data", {}))
            )

# protected

# end
