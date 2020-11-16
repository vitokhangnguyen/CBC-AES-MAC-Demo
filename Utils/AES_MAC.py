import os
from dotenv import load_dotenv
from base64 import b64encode, b64decode
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
load_dotenv()

AES_MAC_Key = bytearray(os.getenv('AES_MAC_SecretKey'), 'utf-8')

def generateMAC(data):
    data = bytearray(data, 'utf-8')
    cmac = CMAC.new(AES_MAC_Key, ciphermod=AES)
    cmac.update(data)
    macTag = cmac.hexdigest()
    return macTag

def verifyMAC(data, tag):
    data = bytearray(data, 'utf-8')
    tag = bytearray(tag, 'utf-8')
    cmac = CMAC.new(AES_MAC_Key, ciphermod=AES)
    cmac.update(data)
    cmac.hexverify(tag)