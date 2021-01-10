#!/usr/bin/env python3
import sys
import mymail

recipient = sys.argv[1]
subject = sys.argv[2]
with open(sys.argv[3]) as file:
    mssg_content = file.read()

mymail.send_mail(recipient, subject, mssg_content)
print("Message sent!")
