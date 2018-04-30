import smtplib
from email.mime.text import MIMEText

mail = 'stason6162s@gmial.com'
msg = MIMEText('Text message')
msg['Subject'] = 'Test Message'
msg['From'] = mail
msg['To'] = mail

# print(msg.as_string())
s = smtplib.SMTP('')
s.sendmail(mail, [mail], msg.as_string())
s.quit()
