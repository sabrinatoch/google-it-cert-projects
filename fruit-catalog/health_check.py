#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
import emails

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
    recipient = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    if not check_CPU_usage:
        emails.generate_email(sender,
                              recipient,
                              "Error - CPU usage is over 80%",
                              body)
    if not check_disk_space:
        emails.generate_email(sender,
                              recipient,
                              "Error - Available disk space is less than 20%",
                              body)
    if not check_memory:
        emails.generate_email(sender,
                              recipient,
                              "Error - Available memory is less than 500MB",
                              body)
    if not check_localhost:
        emails.generate_email(sender,
                              recipient,
                              "Error - localhost cannot be resolved to 127.0.0.1",
                              body)

main()
