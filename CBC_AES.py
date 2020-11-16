import os
from dotenv import load_dotenv
from base64 import b64encode, b64decode
from Padding import pad, unpad
from Crypto.Cipher import AES
load_dotenv()

CBCAESKey = bytearray(os.getenv('CBC_AES_SecretKey').encode('utf-8'))

def encrypt(plaintext):
    plaintext = bytearray(plaintext, 'utf-8')
    plaintext = pad(plaintext, AES.block_size)
    cipher = AES.new(CBCAESKey, AES.MODE_CBC)
    ciphertext = cipher.encrypt(plaintext)
    iv = b64encode(cipher.iv).decode('utf-8')
    ciphertext = b64encode(ciphertext).decode('utf-8')
    return iv, ciphertext

def decrypt(iv, ciphertext):
    iv = b64decode(iv)
    ciphertext = b64decode(ciphertext)
    cipher = AES.new(CBCAESKey, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext, AES.block_size)
    return plaintext.decode()