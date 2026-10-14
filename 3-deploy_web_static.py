#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""
from fabric.api import env
import importlib

do_pack = importlib.import_module('1-pack_web_static').do_pack
do_deploy = importlib.import_module('2-do_deploy_web_static').do_deploy

env.hosts = ['127.0.0.1']


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
