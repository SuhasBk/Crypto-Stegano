A Python application which implements AES CBC encryption and decryption algorithm with steganography using an image file.
The sender embeds the encrypted message along with the key used for encryption in an image file and sends it as an e-mail attachment to the receiver who downloads the image and executes the decryption script to get back the original message.

Requirements:

pycrypto>=2.6.1
