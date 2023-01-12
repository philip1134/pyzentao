# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import json
from pyzentao.attribute_dict import AttributeDict


class Response:
    """zentao api response"""

    def __init__(self, raw):
        super(Response, self).__init__()

        self.raw = raw
        self.status = None
        self.data = {}

        self.parse()

    def __str__(self):
        """printer"""

        text = ""
        for attr in ("status", "data",):
            text += "%s: %s\n" % (
                attr, str(self.__dict__[attr]))

        return text

# public
    def parse(self):
        """parse raw data, just keep 'status' and 'data'

        in GET response, there we can get {status, data}, but for POST response
        in some zentao version, we get {result, message, ...}, in this case we
        map 'result' to 'status', and pack all the other keys into 'data'
        """

        if isinstance(self.raw, dict):
            if "status" in self.raw:
                self.status = self.raw.pop("status", None)
            else:
                self.status = self.raw.pop("result", None)

            if "data" in self.raw:
                self.data = AttributeDict(
                    json.loads(self.raw.get("data", r"{}"))
                )
            else:
                self.data = self.raw


# end
