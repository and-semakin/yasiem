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

import logging
import socketserver
from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

def normalize(raw):
    return {'raw': raw}

class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        today = datetime.now().strftime('%Y-%m-%d')
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        print( "%s : " % self.client_address[0], str(data))
        result = es.index(index=today, doc_type='event', body=normalize(str(data)))
        if not result['created']:
            logging.info(str(data))

if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")