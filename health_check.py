#!/usr/bin/env python3

 # health_check.py

import shutil
import psutil
import emails
import socket


CPU_err = "Error - CPU usage is over 80%"
disk_err = " Error - Available disk space is less than 20%"
mem_err = " Error - Available memory is less than 500MB"
host_err = " Error - localhost cannot be resolved to 127.0.0.1"

message = ""
l = (psutil.cpu_percent(interval=1))
if (psutil.cpu_percent(interval=1) > 80 ):
  message += (CPU_err)
if (shutil.disk_usage(".").used/shutil.disk_usage(".").total) > 0.8:
  message += (disk_err)
if (psutil.virtual_memory().available < (500 * 1024 * 1024)): #500MB
  message += (mem_err)
if not(socket.gethostbyname("localhost") == "127.0.0.1"):
  message += (host_err)

if not  message == "":
  msg = emails.gen_mail_alert(message)
  emails.send_email(msg)
