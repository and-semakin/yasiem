#!/usr/bin/env python

# From: https://gist.github.com/nfarrar/884c72ec107a00606a86 

import argparse
import logging
import logging.handlers
import random
from time import sleep
from datetime import datetime
from datetime import timedelta
from common import *
import random



# import Django; copy from here
import sys
import os
import django
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "webpanel"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webpanel.settings")
django.setup()

from asset.models import (Asset, AssetUser, Alert,
                                   AlertType, OperatingSystem)
# import Django; copy to here


# get all assets and save them to list assets
assets = Asset.objects.all()
# now you can get all the field of object Asset
# name, ipv4, slug, os, user
# see webpanel/asset/models.py
for asset in assets:
    print(asset.name)
for asset in assets:
    print(asset.ipv4)
# get random asset
random_asset = random.choice(assets)
print("Random asset:", random_asset.name, random_asset.ipv4, random_asset.os.name)
exit()


def flood_login(args):
    ACTIONS = ['LOGIN', 'LOGOUT', 'LOGIN FAILED']
    WEIGHTS = [4, 4, 2]
    WORKERS = ["worker"+str(i) for i in range(args.workers)]
    
    logging.basicConfig(level=logging.DEBUG)
    syslogger = logging.getLogger('SyslogLogger')
    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    syslogger.addHandler(handler)
    
    """# modifications
    d = timedelta(seconds = 300)
    dt= datetime.now()"""
    
    for i in range(args.repeats):
        time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        worker = random.choice(WORKERS)
        action = random.choices(ACTIONS, WEIGHTS)[0]
        msg = "%OS-Login% {} {} {}".format(time, worker, action)
        if action == 'LOGIN' or action == 'LOGOUT':
            syslogger.log(string_to_level("INFO"), msg)
        else:
            syslogger.log(string_to_level("WARNING"), msg)
        sleep(args.sleep)

if __name__ == "__main__":
    args = parser.parse_args()
    flood_login(args)
    
    """for i in range(args.repeats):
        time = dt.strftime('%Y-%m-%d-%H-%M-%S-%f')
        dt = dt - d
        
        worker = random.choice(WORKERS)
        action = random.choices(ACTIONS, WEIGHTS)[0]
        msg = "%OS-Login% {} {} {}".format(time, worker, action)
        if action == 'LOGIN' or action == 'LOGOUT':
            syslogger.log(string_to_level("INFO"), msg)
        else:
            syslogger.log(string_to_level("WARNING"), msg)
        sleep(args.sleep)

if __name__ == "__main__":
    args = parser.parse_args()
    flood_login(args)
    """
