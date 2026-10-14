#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['127.0.0.1']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_ext)

        put(archive_path, '/tmp/{}'.format(file_name))
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True
    except Exception:
        return False
