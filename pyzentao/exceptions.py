# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-08-01
#


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

# end
