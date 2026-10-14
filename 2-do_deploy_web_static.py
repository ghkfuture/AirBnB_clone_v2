#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import put, run, env
import os

# TODO: Replace these with your actual web-01 and web-02 server IP addresses!
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        name_no_ext = os.path.splitext(filename)[0]
        release_path = f"/data/web_static/releases/{name_no_ext}"

        put(archive_path, f"/tmp/{filename}")
        run(f"mkdir -p {release_path}/")
        run(f"tar -xzf /tmp/{filename} -C {release_path}/")
        run(f"rm /tmp/{filename}")
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_path}/ /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception:
        return False
