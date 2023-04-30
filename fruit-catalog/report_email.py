#!/usr/bin/env python3

import reports
import emails
import os, glob
import datetime

def write_pdf():
    names = []
    weights = []
    for file in glob.glob("/supplier-data/descriptions/*"):
         with open(file, 'rb') as f:
             line = f.readlines().strip('\n')
             name = line[0]
             weigth = line[1]
             names.append('name: ' + name)
             weights.append('weight: ' + weigth)
    obj = ""
    for i in range(len(names)):
        obj += names[i] + '<br />' + weights[i] + '<br / ><br />'
    return obj



if __name__ == "__main__":
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on " + str(current_date) 
    reports.generate_report('tmp/processed.pdf', title, write_pdf())
    message = emails.generate_email("automation@example.com",
                                    "username@example.com",
                                    "Fruit Catalog Complete",
                                    "All fruits have been uploaded. PDF attached.",
                                    '/tmp/processed.pdf')
    emails.send_email(message)