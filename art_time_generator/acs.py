#!/usr/bin/env python

# From: https://gist.github.com/nfarrar/884c72ec107a00606a86 

import argparse
import logging
import logging.handlers
import random
import json
from time import sleep
from datetime import datetime
from datetime import timedelta
from common_once import *
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
"""# import Django; copy to here


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
exit()"""


def flood_acs(args):
    directions = ['IN', 'OUT']
    users = ["user"+str(i) for i in range(args.workers)]
    
    logging.basicConfig(level=logging.DEBUG)
    syslogger = logging.getLogger('SyslogLogger')
    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    syslogger.addHandler(handler)
    
    """# modifications
    d = timedelta(seconds = 300)
    dt= datetime.now()"""
    
    assets = Asset.objects.all()
    
    print("repeats", args.repeats)
    print("sleep", args.sleep)
    for i in range(args.repeats):
        random_asset = random.choice(assets)
        # print("AZAZLO")
        # print(dir(random_asset))
        # print("AZAZLO")
        
        time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        ipv4 = random_asset.ipv4
        arm = random_asset.name
        os = random_asset.os
        user = random_asset.user
        direction = random.choice(directions)
        msg = "%AccessControl%;{};{};{};{};{};{}".format(time, ipv4, arm, os, user, direction)
        syslogger.log(string_to_level('INFO'), msg)
        sleep(args.sleep)
        print("added", msg)

if __name__ == "__main__":
    args = parser.parse_args()
    flood_acs(args)
    
