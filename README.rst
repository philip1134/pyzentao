========
pyzentao
========

.. image:: https://travis-ci.org/philip1134/pyzentao.svg?branch=master
   :target: https://travis-ci.org/philip1134/pyzentao
   :alt: Build Status

.. image:: https://img.shields.io/pypi/v/pyzentao.svg?color=orange
   :target: https://pypi.python.org/pypi/pyzentao
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pyzentao.svg
   :target: https://pypi.org/project/pyzentao/
   :alt: Supported Python versions

``pyzentao`` 是禅道API的Python SDK，将禅道API映射成为Python方法，例如：

.. code:: text

    GET  /zentao/user-task-[userID]-[type]-[recTotal]-[recPerPage]-[pageID].json

被映射成为 ``Zentao.user_task(...)``

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao(
        "url": "http://my.zentao.site",
        "version": "15",
        "username": "admin",
        "password": "123456",
    )

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy",
        ...
    )

Install and update using ``pip``
--------------------------------

.. code:: text

    $ pip install -U pyzentao

Usage
-----

举个栗子

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao(
        "url": "http://my.zentao.site",
        "version": "15",
        "username": "admin",
        "password": "123456",
    )

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy"
    )

初始化 ``Zentao`` 对象时的参数说明如下

.. code:: text

    url: 禅道站点的域名，包含到
    version: 禅道版本号，不同的禅道版本其API格式不同
    username: 登录禅道的帐号用户名，该帐号最好具有管理员权限
    password: 登录禅道的帐号密码
    spec:   自定义的API规则，选填
        path: 存放自定义规则的路径或者文件路径，须为yaml文件
        merge: 合并方式，True 表示与默认规则合并
