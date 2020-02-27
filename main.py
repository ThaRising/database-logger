#!/usr/bin/python3.7
# !python3
# -*- coding: utf-8 -*-

from application import *
import sys

if __name__ == "__main__":
    application_parameters = get_console_args(sys.argv[1:])
    logfile = File(application_parameters)
    logfile.parse()
    logfile.dump()
