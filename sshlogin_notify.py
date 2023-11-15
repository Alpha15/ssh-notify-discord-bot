import os
from datetime import datetime

LOGFILE = "/tmp/shellscript_auth.log"

def date_time(line):
    timestamp_list = line.split()[:3]
    print(timestamp_list)
