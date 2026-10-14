#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from web_static folder"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generates a tgz archive from web_static folder"""
    if not os.path.exists("versions"):
        os.makedirs("versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"
    print(f"Packing web_static to {archive_path}")
    result = local(f"tar -cvzf {archive_path} web_static")
    if result.succeeded:
        return archive_path
    return None
