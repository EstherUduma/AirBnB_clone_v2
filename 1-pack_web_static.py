#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    # Get the current UTC time for the filename
    dt = datetime.utcnow()

    # Define the filename for the archive
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)

    # Create the "versions" directory if it doesn't exist
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    # Create the tar gzipped archive
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None

    # Return the path to the created archive
    return file
