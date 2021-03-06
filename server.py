from os import stat, stat_result
from flask import Flask, request
import flask
from flask.wrappers import Response
from Utils.Logging import logMessage
import Utils.CBC_AES as CBC_AES
import Utils.AES_MAC as AES_MAC

app = Flask(__name__)

@app.route('/cbc-aes/mac-decrypt')
def CBC_AES_MAC_Decrypt():
    # Get query parameters
    iv = request.args.get('iv')
    encryptedMessage = request.args.get('encryptedMessage')
    macTag = request.args.get('macTag')
    try:
        AES_MAC.verifyMAC(encryptedMessage, macTag) # Throw exception when MAC fails
        message = CBC_AES.decrypt(iv, encryptedMessage)
        logMessage(message, useMac=True)
        print(f'========== Message Received ===========')
        print(message)
        return 'Message received, verified and decrypted successfully'
    except:
        return flask.Response('Fail to receive message', status=500)



@app.route('/cbc-aes/decrypt')
def CBC_AES_Decrypt():
    # Get query parameters
    iv = request.args.get('iv')
    encryptedMessage = request.args.get('encryptedMessage')

    message = CBC_AES.decrypt(iv, encryptedMessage)
    logMessage(message)
    print(f'========== Message Received ===========')
    print(message)
    return 'Message received and decrypted successfully'