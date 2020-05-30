import smtplib
import ssl

# author   -> albwrekt
# date     -> 5/30/2020
# revision -> 1.0.0
# 

# opens a file with the following format
# Line 1: sending email
# Line 2: sending email's password
# Line 3: receiving email
# Note that this program was used with a sending gmail to debug


class EmailGenerator:

    # This method generates a gmail bot to send emails.
    # PARAM filename -> filepath of the email information text document as specified above.  
    def __init__(self, filename):
        self.ssl_context = ssl.create_default_context()
        email_info = open(filename, "r")
        info_list = list()
        for info in email_info:
            info_list.append(info)
        self.port = 465
        self.smtp_server = 'smtp.gmail.com'
        self.ready = len(info_list) == 3
        if self.ready:
            self.sender_email = info_list[0]
            self.password = info_list[1]
            self.receiver_email = info_list[2]
            self.server = smtplib.SMTP_SSL(
            self.smtp_server, self.port, context=self.ssl_context)
            self.server.login(self.sender_email, self.password)
        else:
            print("The email server was not opened due to improperly provided information in the specified file.")

    # This method sends a specified message if the email server is logged in and ready
    # PARAM subject -> the subject of the email
    # PARAM message -> the message to be sent, three quote string
    def send_text_mail(self, subject, message):
        if self.ready:
            self.server.sendmail(self.sender_email, self.receiver_email,
                    """Subject: """ + subject + """\n\n""" + message.replace("'", ""))
