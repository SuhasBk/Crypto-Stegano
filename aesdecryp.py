#!/usr/bin/python3
from Crypto.Cipher import AES

f = open(input("Enter the image name sent by the sender... : (without the extension)\n")+'.jpg','rb')
send_data = f.read()

recv_key = send_data[len(send_data)-16 : ]
recv_msg = send_data[len(send_data)-48 : len(send_data)-32]
recv_iv = send_data[len(send_data)-32 : len(send_data)-16]

aes_dec = AES.new(recv_key,AES.MODE_CBC,recv_iv)
dec = aes_dec.decrypt(recv_msg)

print('HIDDEN MESSAGE : '+dec.decode('utf-8'))
