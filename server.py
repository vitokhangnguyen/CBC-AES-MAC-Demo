import json
from flask import Flask, request
import CBC_AES
app = Flask(__name__)

@app.route('/cbc-aes/decrypt')
def CBC_AES_Decrypt():
    iv = request.args.get('iv')
    encryptedMessage = request.args.get('encryptedMessage')
    message = CBC_AES.decrypt(iv, encryptedMessage)
    print(f'========== Received: {message} ===========')
    return 'Message received and decrypted successfully'