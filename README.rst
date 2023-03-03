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

在调用方法时，``pyzentao`` 会根据初始化时输入的配置参数获取禅道的授权，然后调用对应的API，并返回数据结果。


安装
----

.. code:: text

    $ pip install -U pyzentao

使用时需要根据你家的禅道版本指定 API 规格，自 ``pyzentao r0.4.0`` 版本之后，规格文件由
`pyzentao-specs <https://github.com/philip1134/pyzentao-specs>`__ 项目维护，
在该项目下载对应的规格文件，放到你的项目下，初始化时指向这个路径即可，详见 ``pyzentao-specs`` 的说明。

也可以使用 `miaou <https://github.com/philip1134/miaou>`__ 自助生成规格文件。

用法
----

上栗子
~~~~~~

查询用户任务
^^^^^^^^^^^^

获取指定用户的任务，原生API为

.. code:: text

    GET  /zentao/user-task-[userID]-[type]-[recTotal]-[recPerPage]-[pageID].json

该API被映射为 ``user_task`` 方法

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao({
        "url": "http://my.zentao.site/zentao",
        "username": "admin",
        "password": "123456",
        "spec": "/path/to/my/project/v17.6"
    })

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy",
        ...
    )

    print(tasks.status) # success
    print(tasks.data) # dict...

创建任务
^^^^^^^^

对于需携带POST参数的API，可使用 ``data`` 传入，例如创建任务，原生API为

.. code:: text

    GET/POST  /zentao/task-create-[projectID]-[storyID]-[moduleID]-[taskID]-[todoID].json

该API被映射为 ``task_create`` 方法

.. code:: python

    import pyzentao

    zentao = pyzentao.Zentao({
        "url": "http://my.zentao.site/zentao",
        "username": "admin",
        "password": "123456",
        "spec": "/path/to/my/project/v17.6"
    })

    response = zentao.task_create(
        executionID=2,
        storyID=0,
        moduleID=0,
        ...
        data={
            "execution": 2,
            "type": "design",
            "name": "锦囊喵叽",
            "assignedTo[]": "老六",
            "pri": 3,
            "desc": "暴打小柯基"
            ...
        },
    )

    print(response.status) # success

注意，在 POST参数中,使用 ``assignedTo[]`` 指派任务，而不是文档中的 ``assignedTo`` ⊙﹏⊙‖∣

初始化参数说明
~~~~~~~~~~~~~~

初始化 ``Zentao`` 对象时的参数说明如下：

.. code:: text

    url: 禅道站点的域名，一般需要加上 zentao 这个前缀，如 http://my.zentao.site/zentao
    username: 登录禅道的帐号用户名，该帐号最好具有管理员权限
    password: 登录禅道的帐号密码
    spec:   API规格文件路径，可以是 yaml 文件路径或是包含规格文件的目录路径

返回数据处理
~~~~~~~~~~~~

禅道原生API的返回数据中字段繁杂，默认情况下 ``pyzentao`` 做了整理，只保留了 ``status`` 和 ``data`` 的数据，
如果需要获得全部原生的数据，可在API调用中加入参数 ``raw=True``，例如

.. code:: python

    tasks = zentao.user_task(
        userID=1,
        type="finishedBy",
        ...
        raw=True
    )

某些 POST API 调用的返回值为 {result, message, ...}，而非 {status, data} 格式，
我们均将其映射为后者，即 result 映射为 status, {message, ...} 赋值为 data 。

其他
~~~~

``pyzentao`` 对于API调用过程中出现的异常并不作捕获，建议业务层根据自身使用场景决定处理逻辑。

如果API的返回数据中不包含合法的json数据，将会抛出 ``InvalidJSONResponseError`` 的异常，
一般原因是返回了HTML格式的数据，如404页面，请确认初始化时的 ``url`` 参数是否正确，或原生API的调用是否正常。

作为懒癌晚期患者，功能仅在 ``Linux/Python3.10`` 环境下测试，不打算兼容 ``Python2`` 和 ``Python3.3`` 以前版本 (๑¯ω¯๑)
