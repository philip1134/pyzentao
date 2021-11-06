========
pyzentao
========

.. image:: https://travis-ci.com/philip1134/pyzentao.svg?branch=master
   :target: https://travis-ci.com/philip1134/pyzentao
   :alt: Build Status

.. image:: https://img.shields.io/pypi/v/pyzentao.svg?color=orange
   :target: https://pypi.python.org/pypi/pyzentao
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pyzentao.svg
   :target: https://pypi.org/project/pyzentao/
   :alt: Supported Python versions

``pyzentao`` 是禅道API的Python SDK，简单封装了禅道API，将其映射成为Python方法，例如：

.. code:: text

    GET  /zentao/user-task-[userID]-[type]-[recTotal]-[recPerPage]-[pageID].json

被映射成为 ``Zentao.user_task(...)`` ，后续 ``[...]`` 里的参数被映射成为调用方法的参数。

在调用方法时，``pyzentao`` 会根据初始化时输入的配置参数获取禅道的授权，然后调用对应的API，并返回原生的数据结果。


Installation
------------

.. code:: text

    $ pip install -U pyzentao

Usage
-----

举个栗子，要获取指定用户的任务，原生API为：

.. code:: text

    GET  /zentao/user-task-[userID]-[type]-[recTotal]-[recPerPage]-[pageID].json

该API被映射为 ``user_task`` 方法：

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao({
        "url": "http://my.zentao.site/zentao",
        "version": "15",
        "username": "admin",
        "password": "123456",
    })

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy",
        ...
    )

    print(tasks.status) # success
    print(tasks.data) # dict...


初始化 ``Zentao`` 对象时的参数说明如下：

.. code:: text

    url: 禅道站点的域名，一般需要加上 zentao 这个前缀，如 http://foo.bar/zentao
    version: 禅道版本号，不同的禅道版本其API格式不同
    username: 登录禅道的帐号用户名，该帐号最好具有管理员权限
    password: 登录禅道的帐号密码
    spec:   自定义的API规则，选填
        path: 存放自定义规则的路径或者文件路径，须为yaml文件
        merge: 合并方式，True 表示与默认规则合并


注意，禅道API的返回数据中如果不包含合法的json数据，将会抛出 ``requests.exceptions.JSONDecodeError`` 的异常，一般原因是返回了HTML格式的数据，如404页面，请确认初始化时的 ``url`` 参数是否正确，或原生API的调用是否正常。
