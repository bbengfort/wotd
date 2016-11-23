#!/usr/bin/env python3
# manage
# WOTD management script
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 10:09:27 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: manage.py [] benjamin@bengfort.com $

"""
WOTD management script
"""

##########################################################################
## Imports
##########################################################################

import os

from app import create_app
from flask_script import Manager


##########################################################################
## Instantiate the Application
##########################################################################

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


##########################################################################
## Main Method
##########################################################################

if __name__ == '__main__':
    manager.run()
