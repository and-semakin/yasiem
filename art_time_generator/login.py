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

def flood_login(args):
    ACTIONS = ['LOGIN', 'LOGOUT', 'LOGIN FAILED']
    WEIGHTS = [4, 4, 2]
    WORKERS = ["worker"+str(i) for i in range(args.workers)]
    
    logging.basicConfig(level=logging.DEBUG)
    syslogger = logging.getLogger('SyslogLogger')
    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    syslogger.addHandler(handler)
    
    # modifications
    d = timedelta(seconds = 300)
    dt= datetime.now()
    
    for i in range(args.repeats):
        # modifications
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
    
