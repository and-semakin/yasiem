import argparse
import random
import logging
import logging.handlers
from time import sleep
from datetime import datetime
from datetime import timedelta
from common import *
from elasticsearch import Elasticsearch

def search_only_in():
    es = Elasticsearch()
    reply = es.search(index="events", doc_type="event_document",
    body={
        "query":
            {"match":
                {"act": "IN"}
            }
    })
    print(reply)

"""def search_only_user():
    es = Elasticsearch()
    reply = es.search(index="events", doc_type="event_document",
    body={
        "query":
            {"match":
                {"user": "ПК Шепарда"}
            }
    })
    print(reply)"""

def drop_db():
    es = Elasticsearch()
    es.indices.delete(index="events", ignore=[400, 404])
    print("es db was dropped %)")

if __name__ == "__main__":
    # search_only_in()
    # search_only_user()
    # drop_db()
    exit()
    
    
    """
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
        sleep(args.sleep)"""