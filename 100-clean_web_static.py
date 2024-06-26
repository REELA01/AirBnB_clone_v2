#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py"""
from fabric.api import *


env.hosts = ['34.232.67.200', '34.237.91.14']
env.user = "ubuntu"


def do_clean(number=0):
    """do clean"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
