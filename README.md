Sends an SMS with any email addresses that signed up on your Launchrock landing page

To run:
 1. git clone https://github.com/dhruvkar/launchrock-notifications.git
 1. Add a config.py file with the following variables:
   * `lr_url`: URL for the "export as CSV" link (see picture below)
   * `user_email`: Email used for logging into launchrock.com
   * `user_pw`: Password used for logging into launchrock.com
   * `msg_me = 'curl http://textbelt.com/text -d number=XXXXXXXXXX -d "message=New signup(s): '`: Replace the Xs with your phone number
 1. `python launchrock_emails.py`

This will create a signups.txt file with emails that have already signed up. It will also text you with all those email addresses the first time.

![Launchrock export link](/launchrock-notifications/launchrock_export.png)
