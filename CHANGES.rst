Mini-MO Changelog
=================

Here you can see the full list of changes between each mini-mo release.


Version 0.8.2
-------------

Released on 2021-07-13

- scheduler: job store configurable
- scheduler: job executor max workers configurable


Version 0.8.1
-------------

Released on 2021-07-04

- fix: omit new folders in manifest.in


Version 0.8.0
-------------

Released on 2021-07-03

- introduced scheduler to run scheduled jobs in minimo
- refactored interface
- refactored commands


Version 0.7.5
-------------

Released on 2021-02-03

- load config yaml file with encoding utf8


Version 0.7.4
-------------

Released on 2020-12-31

- template: add absolute module path from cases folder


Version 0.7.3
-------------

Released on 2020-12-30

- convert case name to full module name


Version 0.7.2
-------------

Released on 2020-12-30

- wrong LICENSE file name set in installation package


Version 0.7.1
-------------

Released on 2020-12-29

- log format changed
- upgrade attribute dict


Version 0.7.0
-------------

Released on 2020-11-26

- yaml for case config
- config option to redirect stdout to log file
- bug-fix: max thread count not works in concorrence mode


Version 0.6.1
-------------

Released on 2020-09-07

- bug-fix: add project instance path to sys.path for api mode


Version 0.6.0
-------------

Released on 2020-04-24

- run suite/cases with multiprocessing thread pool under `concorrence` mode


Version 0.5.4
-------------

Released on 2020-04-17

- bug-fix: basestring not defined in python3, use str instead
- bug-fix: load config module from current case in case template file
- remove 0.5.3 due to duplicated release


Version 0.5.2
-------------

Released on 2019-07-24

- run suite/cases with multiprocess pool under `concorrence` mode
- bug-fix: unicode not defined in python3


Version 0.5.1
-------------

Released on 2019-07-15

- README updated
- add `call` to call minimo main function in api mode


Version 0.5.0
-------------

Released on 2019-07-11

- compatible with python 3


Version 0.4.1
-------------

Released on 2019-07-03

- markdown to rst
- add option to allow specify output path while creating project

Version 0.4.0
-------------

Released on 2019-06-19

- add cli alias: mmo
- `api` mode enabled and its usage in README
- bug-fix: wrong package name for PyYAML in setup dependencies


Version 0.3.1
-------------

Released on 2018-12-19

- logger: print report to report file
- logger: interface to get log dir path
- bug-fix: convert new line not work while creating file with template


Version 0.3.0
-------------

Released on 2018-11-02

- use mako filter to customize template
- add "ls" command to list all standard cases
- introduced `click` to organize cli
- remove locales


Version 0.2.1
-------------

Released on 2018-05-21

- help string for init, add project template list
- revert to mako template
- migrations for flask template


Version 0.2.0
-------------

Released on 2018-04-13

- classified commands by project type
- supported project type: task, flask


Version 0.1.2
-------------

Released on 2018-03-28

- allow customized logger for performer
- command to print minimo version number


Version 0.1.1
-------------

Released on 2018-03-05

- init project by templates
- locale supported
- run tasks by serial or concorrence type


Version 0.1.0
-------------

First public preview release.