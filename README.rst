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

目前支持禅道开源版:

    - v17.6
    - v16.5
    - v15.7
    - v15.2
    - v12.5.3

也可以自定义API规格


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

    url: 禅道站点的域名，一般需要加上 zentao 这个前缀，如 http://my.zentao.site/zentao
    version: 禅道版本号，支持 'v17.6', 16.5', '15.7', '15' (15.2) 和 '12' (12.5.3)等。不同的禅道版本其API格式不同，默认取值 '15'
    username: 登录禅道的帐号用户名，该帐号最好具有管理员权限
    password: 登录禅道的帐号密码
    spec:   自定义的API规则，选填
        path: 存放自定义规格的路径或者文件路径，须为yaml文件
        merge: 合并方式，默认为 True 表示与默认规则合并

对于暂未默认支持的禅道版本，可使用 ``spec`` 指定自定义的API规格，例如

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao({
        "url": "http://my.zentao.site/zentao",
        "username": "admin",
        "password": "123456",
        "spec": {
            "path": "path/to/spec", # 存放规格文件的地址，可以指向目录或单个文件
            "merge": False # 默认取值 True 会合并到 15 版本
        }
    })

规格文件应为 yaml 文件，格式如

.. code:: yaml

    user_task:
        method: GET
        path: user-task
        params:
            - userID
            - type
            - recTotal
            - recPerPage
            - pageID
    ...

对于未支持的禅道分支版本，可以使用 ``merge: True`` 的方式合并规格，合并时使用了 ``dict.update(...)``，
对于原生API中方法为 ``GET/POST`` 的接口均使用 ``POST`` 方法调用。

禅道原生API的返回数据中字段繁杂，默认情况下 ``pyzentao`` 做了整理，只保留了 ``status`` 和 ``data`` 的数据，
如果需要获得全部原生的数据，可在API调用中加入参数 ``raw=True``，例如

.. code:: python

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy",
        ...
        raw=True
    )


``pyzentao`` 对于API调用过程中出现的异常并不作捕获，建议业务层根据自身使用场景决定处理逻辑。

如果API的返回数据中不包含合法的json数据，将会抛出 ``InvalidJSONResponseError`` 的异常，
一般原因是返回了HTML格式的数据，如404页面，请确认初始化时的 ``url`` 参数是否正确，或原生API的调用是否正常。

作为懒癌晚期患者，功能仅在 ``Linux/Python3.10`` 环境下测试，不打算兼容 ``Python2`` 和 ``Python3.3`` 以前版本 (๑¯ω¯๑)
