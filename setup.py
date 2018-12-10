# -*- coding: utf-8 -*-
# @Time    : 18-10-22 下午3:38
# @Author  : Redtree
# @File    : setup.py
# @Desc :

from setuptools import setup, find_packages

setup(
    name = "redflask",
    version = "0.1.5",
    keywords = ("pip", "flask","restful", "redflask", "cli"),
    description = "Restful framework base on flask without blueprint",
    long_description = "A Restful_Api service framework based on Flask, which implements routing separation "
                       "without relying on Flask's blueprint. It provides a common interface between HTTP request"
                       " types and file transfer types.A simpler asynchronous task distribution scheme is provided. "
                       "The most commonly used user password verification module and token verification module are provided. "
                       "The server's automatic configuration scheme is integrated with Gunicorn+Gevent."
                       " Database useSqlalchemy and Redis. Provides a solution for Flask as a Https service. The Flask cross domain problem is solved.",
    license = "MIT Licence",

    url = "https://gitee.com/sleepingtree/red_flask",
    author = "redtree",
    author_email = "redtree@aliyun.com",

    packages = find_packages(),
    entry_points='''
    [console_scripts]
    redflask = redflask.main:main
    ''',
    include_package_data = True,
    platforms = "linux",
    install_requires = ['Flask','pymysql','Sqlalchemy','Gunicorn','Gevent','redis','requests']
)



