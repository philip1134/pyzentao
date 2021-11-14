# -*- coding:utf-8 -*-
#
# author: philip1134
# date: 2021-07-15
#


import copy


class SimpleAttributeDict(dict):
    """Works like dict but provides methods to get attribute by '.'.

    such as::
        attrDict = SimpleAttributeDict({'foo': foo, 'bar': bar})
        print(attrDict.foo)
        attrDict.bar = bar2
    """

    def __init__(self, defaults={}):
        super(SimpleAttributeDict, self).__init__(defaults)
        # dict.__init__(self, defaults)

    def __getattr__(self, attrname):
        return self.get(attrname)

    def __setattr__(self, attrname, value):
        self[attrname] = value

    def __deepcopy__(self, memo):
        return SimpleAttributeDict(copy.deepcopy(self.copy(), memo))


class AttributeDict(dict):
    """Works like dict but provides methods to get attribute by '.',
    inspired by EasyDict of Mathieu Leplatre

    such as::
        attrDict = AttributeDict({'foo': foo, 'bar': bar})
        attrDict.foo    # => foo
        attrDict.bar = bar2
    """

    def __init__(self, defaults={}):
        # super(AttributeDict, self).__init__(defaults)

        defaults = defaults or {}
        for k, v in defaults.items():
            setattr(self, k, v)

        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')) and \
               k not in ('update', 'pop'):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, self.__class__):
            value = self.__class__(value)

        super(AttributeDict, self).__setattr__(name, value)
        super(AttributeDict, self).__setitem__(name, value)

    def __deepcopy__(self, memo):
        return AttributeDict(copy.deepcopy(self.copy(), memo))

    __setitem__ = __setattr__

    def update(self, other=None):
        other = other or dict()
        for k in other:
            setattr(self, k, other[k])

    def pop(self, k, default=None):
        delattr(self, k)
        return super(AttributeDict, self).pop(k, default)

# end
