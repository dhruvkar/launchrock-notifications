import requests
import re
import os
from config import *

# Get the csv from Launchrock and return it as a list
def get_csv(launchrock_url):
    r = requests.get(lr_url, auth=(user_email, user_pw))
    if r.status_code == 200:
        csv_emails = re.findall(r'[a-zA-Z0-9_.-]{0,20}@[a-zA-Z0-9_.-]{0,20}.[a-zA-Z0-9_.-]{1,10}', r.text)
        return csv_emails
    else:
        return "couldn't authenticate"

# Extract emails from existing list and return a list; or create a new file if it doesn't exist
def extract_emails(signups_file):
    try:
        with open(signups_file) as f:
            lines = [line.rstrip('\n') for line in f]
    except:
        os.system('touch '+signups_file)
        with open(signups_file) as f:
            lines = [line.rstrip('\n') for line in f] 
    return lines

# Add and text me the new email addresses into list
def add_new_emails(new_emails, email_list):
    message = ''
    for new_email in new_emails:
        if new_email not in email_list:
            email_list.append(new_email)
            message = message+new_email+', '
    if message:
        os.system(msg_me+message+'"')
    return email_list



# Write the new list into a file
def write_list_to_file(email_list, filename):
    f = open(filename, 'w')
    for email in email_list:
            f.write(email+'\n')
    f.close()


csv_emails = get_csv(lr_url)
existing_emails = extract_emails('signups.txt')
updated_email_list = add_new_emails(csv_emails, existing_emails)
write_list_to_file(updated_email_list, 'signups.txt')
