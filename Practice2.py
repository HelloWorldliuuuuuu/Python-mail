from email.header import Header
from email.mime.text import MIMEText
import smtplib
import csv

file ='email.csv'
with open(file, "r", encoding="ISO-8859-1") as csv_file:  
    read = csv.reader(csv_file)
    for line in read:
        to_addr =line[1]
print('Sending email .........')
from_addr ='XXXXXX@qq.com'
#¿¼ÂÇµ½ÒşË½´Ë´¦ÌîĞ´ÄãµÄ·¢ËÍÓÊÏäµØÖ·£¨QQÓÊÏä£©
password = 'XXXXXXX'
#¿¼ÂÇµ½ÒşË½´Ë´¦ÌîĞ´ÄãQQÓÊÏäµÄÊÚÈ¨Âë
print('recevier:' + to_addr)
smtp_server = 'smtp.qq.com'
msg = MIMEText('Practice2,csv,smtplib','plain','utf-8')
msg['From'] =from_addr
msg['To'] = to_addr
msg['Subject'] = Header('Send by Python','utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print('Email has been sent')
