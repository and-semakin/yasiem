import argparse
import random
import logging
import logging.handlers
from time import sleep
from datetime import datetime
from datetime import timedelta
from common import *

if __name__ == "__main__":
    
    args = parser.parse_args()
    
    ACTIONS = ['LOGIN FAILED']
    WEIGHTS = [1]
    WORKERS = ["worker"+str(i) for i in range(args.workers)]
    
    logging.basicConfig(level=logging.DEBUG)
    syslogger = logging.getLogger('SyslogLogger')
    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    syslogger.addHandler(handler)
    
    d = timedelta(seconds = 2)
    dt= datetime.now()
    
    worker = random.choice(WORKERS)
    
    for i in range(args.repeats):
        # modifications
        time = dt.strftime('%Y-%m-%d-%H-%M-%S-%f')
        dt = dt - d
        
        action = random.choices(ACTIONS, WEIGHTS)[0]
        msg = "%OS-Login% {} {} {}".format(time, worker, action)
        if action == 'LOGIN' or action == 'LOGOUT':
            syslogger.log(string_to_level("INFO"), msg)
        else:
            syslogger.log(string_to_level("WARNING"), msg)
        sleep(args.sleep)