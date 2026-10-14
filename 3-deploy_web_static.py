#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""
from fabric.api import env
from importlib import import_module

pack_module = import_module('1-pack_web_static')
deploy_module = import_module('2-do_deploy_web_static')

# TODO: Replace these with your actual web-01 and web-02 server IP addresses!
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = pack_module.do_pack()
    if not archive_path:
        return False
    return deploy_module.do_deploy(archive_path)
