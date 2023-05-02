#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
import emails

user = os.getenv('USER')

def check_disk_space():
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    return free > 20

def check_CPU_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_memory():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost=="127.0.0.1"

def main():
    sender = "aumation@example.com"
    recipient = "{}@example.com".format(user)
    body = "Please check your system and resolve the issue as soon as possible."

    if not check_CPU_usage():
        msg = emails.generate_email(sender,
                              recipient,
                              "Error - CPU usage is over 80%",
                              body)
        emails.send_email(msg)
    if not check_disk_space():
        msg = emails.generate_email(sender,
                              recipient,
                              "Error - Available disk space is less than 20%",
                              body)
        emails.send_email(msg)
    if not check_memory():
        msg = emails.generate_email(sender,
                              recipient,
                              "Error - Available memory is less than 500MB",
                              body)
        emails.send_email(msg)
    if not check_localhost():
        msg = emails.generate_email(sender,
                              recipient,
                              "Error - localhost cannot be resolved to 127.0.0.1",
                              body)
        emails.send_email(msg)

main()
