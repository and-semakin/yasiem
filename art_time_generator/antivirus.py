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

def flood_antivirus(args):
    RESULTS = ['CLEAN', 'INFECTED FIXED', 'INFECTED MOVED']
    WEIGHTS = [90, 2, 8]
    FILES = ["document_{}.docx".format(i) for i in range(args.files)]
    PCS = ["PC{}".format(i) for i in range(args.pcs)]
    
    logging.basicConfig(level=logging.DEBUG)
    syslogger = logging.getLogger('SyslogLogger')
    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    syslogger.addHandler(handler)
    
    # modifications
    d = timedelta(seconds = 300)
    dt = datetime.now()
    
    for i in range(args.repeats):
        # modifications
        time = dt.strftime('%Y-%m-%d-%H-%M-%S-%f')
        dt = dt - d
        
        filename = random.choice(FILES)
        result = random.choices(RESULTS, WEIGHTS)[0]
        pc = random.choice(PCS)
        msg = "%Antivirus% {} {} {} {}".format(time, pc, filename, result)
        if result == 'INFECTED FIXED' or result == 'INFECTED MOVED':
            syslogger.log(string_to_level("CRITICAL"), msg)
        else:
            syslogger.log(string_to_level("INFO"), msg)
        sleep(args.sleep)

if __name__ == "__main__":
    args = parser.parse_args()
    flood_antivirus(args)
    
