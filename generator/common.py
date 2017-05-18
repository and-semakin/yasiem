#!/usr/bin/env python

# From: https://gist.github.com/nfarrar/884c72ec107a00606a86 

import argparse
import logging
import logging.handlers
import random
from time import sleep
from datetime import datetime

default_address = "localhost"
default_port = 514
default_level = "INFO"
default_repeats = 50
default_sleep = 2

parser = argparse.ArgumentParser(__file__,
                                 description="A syslog message generator")

parser.add_argument("--address",
                    "-a",
                    default=default_address,
                    help="The syslog message recipient address")

parser.add_argument("--port",
                    "-p",
                    type=int,
                    default=default_port,
                    help="The syslog message recipient port")

parser.add_argument("--level",
                    "-l",
                    default=default_level,
                    help="The syslog message log level")

parser.add_argument("--message",
                     "-m",
                    help="The syslog message")

parser.add_argument("--repeats",
                    "-r",
                    type=int,
                    default=default_repeats,
                    help="Number of repeats")

parser.add_argument("--sleep",
                    "-s",
                    type=int,
                    default=default_sleep,
                    help="Sleep between repeats")

parser.add_argument("--workers",
                    "-w",
                    type=int,
                    default=20,
                    help="Number of workers")

parser.add_argument("--files",
                    "-f",
                    type=int,
                    default=1000,
                    help="Number of files")

parser.add_argument("--pcs",
                    "-c",
                    type=int,
                    default=20,
                    help="Number of PCs")

def string_to_level(log_level):
    """ Convert a commandline string to a proper log level
    @param string log_level     command line log level argument
    @return logging.LEVEL       the logging.LEVEL object to return
    """
    if log_level == "CRITICAL":
        return logging.CRITICAL
    if log_level == "ERROR":
        return logging.ERROR
    if log_level == "WARNING":
        return logging.WARNING
    if log_level == "INFO":
        return logging.INFO
    if log_level == "DEBUG":
        return logging.DEBUG
    return logging.NOTSET
