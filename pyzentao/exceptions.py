# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-08-01
#


_splitter = "-" * 20


class PyZentaoException(Exception):
    """pyzentao base exception class"""

    pass


class AuthenticationError(PyZentaoException):
    """exception for authentication error"""

    pass


class APINameError(PyZentaoException):
    """exception for unknown api name error"""

    def __init__(self, name):
        super(APINameError, self).__init__()

        self.name = name

    def __str__(self):
        """printer"""

        return "Unknown API name '%s'" % self.name


class InvalidJSONResponseError(PyZentaoException):
    """exception for invalid json in response error"""

    def __init__(self, response):
        super(InvalidJSONResponseError, self).__init__()

        self.response = response

    def __str__(self):
        """printer"""

        return """
Invalid object type or invalid json in api response, that may raise
json.decoder.JSONDecodeError, the original response is:
%s\n%s\n%s\n""" % (_splitter, self.response, _splitter)


# end
