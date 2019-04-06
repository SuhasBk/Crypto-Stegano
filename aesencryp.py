#!/usr/bin/python3
import os
from getpass import getpass
import smtplib
from Crypto.Cipher import AES
from email.message import EmailMessage

email = os.environ.get('EMAIL')         #enter your email and password here
passwd = os.environ.get('PASSWORD')

key,iv = os.urandom(16),os.urandom(16)

original_data = getpass("Enter the '16-byte' message to be encrypted:\n")

if len(original_data)>16:
    original_data = original_data[:16]
elif len(original_data)<16:
    for i in range(16-len(original_data)):
        original_data+=' '

original_data = str.encode(original_data)

with open(input("Enter the path to an image file:\n"),'rb') as f:
    dummy_data = f.read()

aes_enc = AES.new(key,AES.MODE_CBC,iv)
enc = aes_enc.encrypt(original_data)

send_data = dummy_data + enc + iv + key         #true power of python lies here

msg = EmailMessage()
msg['To'] = input("Enter the email-ID of the receiver : \n")
msg['Subject'] = 'Cryptography Demo'
msg['From'] = email
msg.set_content(str(input("Type any extra message or instructions to be sent?\n")))
msg.add_attachment(send_data, maintype='image', subtype='jpeg', filename=input("Enter the name of the image to be sent : (without the extension)\n")+'.jpg')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email,passwd)
    smtp.send_message(msg)

exit('The message has been successfully encrypted, embedded and sent!')
