#!/usr/bin/env python

# From: https://gist.github.com/nfarrar/884c72ec107a00606a86 

import random
from datetime import datetime
from common import *
from multiprocessing import Process
from time import sleep

from acs import flood_acs
from login import flood_login
from antivirus import flood_antivirus

if __name__ == "__main__":
    args = parser.parse_args()
    
    p1 = Process(target=flood_acs, args=(args,))
    p1.start()
    sleep(0.33)    
    p2 = Process(target=flood_login, args=(args,))
    p2.start()
    sleep(0.33)    
    p3 = Process(target=flood_antivirus, args=(args,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print("Finished")
    
