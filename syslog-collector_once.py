#!/usr/bin/env python

## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.

LOG_FILE = 'logs/collector_errors.log'
HOST, PORT = "0.0.0.0", 514

#
# NO USER SERVICEABLE PARTS BELOW HERE...
#
import argparse
import logging
import logging.handlers
import socketserver
from elasticsearch import Elasticsearch
from datetime import datetime
#from normalizer import normalize
from normalizer_once import normalize
from corellator_once import *

counter = 0

es = Elasticsearch()

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global counter
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        print( "%s : " % self.client_address[0], str(data))
        body = normalize(str(data))
        result = es.index(index='events', doc_type='event_document', body=body)
        print("%should be indexed%")
        print("result")
        # check_failed_login()
        # corellate_in_out(body)
        
        if not result['created']:
            logging.info(str(data))
            
            # query to corellator
        else:
            counter += 1
            print("Got", counter, "messages")
        
        

        logging.basicConfig(level=logging.DEBUG)
        syslogger = logging.getLogger('SyslogLogger')
        handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 778), facility=19)
        syslogger.addHandler(handler)
        
        msg = body
        syslogger.log(logging.INFO, msg)

if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")