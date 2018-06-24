#####################################################################
#       Script to send an email with no attachment                  #
#                   Script by:                        #
#                    Dated:                          #
#####################################################################
 
# This script uses a gmail account to send the mail. If you
# have your account with another email provider, you will have
# to change the smtp_variable and smtp_port variable accordingly.
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
# fill in the variables
smtp_server = "smtp.gmail.com"
smtp_port = 587                                 # for smtp.gmail.com
from_address = "ds.deshmukh@gmail.com"              # e.g. username@gmail.com
from_password = "google123#"    # required by script to login using your username
to_address = "des.sachin@gmail.com"                  # e.g. username2@gmail.com
subject = "Subject Tets"               
mail_body = "Body content here"
 
msg = MIMEMultipart()
msg['Subject'] =  subject
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
 
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()
##
