#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import put, run, env
import os

env.hosts = ['52.55.249.213', '54.157.32.137']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    
    try:
        filename = os.path.basename(archive_path)
        name_no_ext = os.path.splitext(filename)[0]
        release_path = f"/data/web_static/releases/{name_no_ext}"

        # 1. Upload the archive to the /tmp/ directory of the web server
        put(archive_path, f"/tmp/{filename}")

        # 2. Uncompress the archive to the release folder
        run(f"mkdir -p {release_path}/")
        run(f"tar -xzf /tmp/{filename} -C {release_path}/")

        # 3. Delete the archive from the web server
        run(f"rm /tmp/{filename}")

        # 4. Move files from nested web_static to release folder
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")

        # 5. Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # 6. Create a new symbolic link linked to the new version
        run(f"ln -s {release_path}/ /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception:
        return False
