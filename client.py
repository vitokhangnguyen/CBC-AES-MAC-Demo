import sys
import requests
import Utils.CBC_AES as CBC_AES
import Utils.AES_MAC as AES_MAC
from Utils.CBC_AES import decrypt

def main():
    if (len(sys.argv) not in (2, 3)):
        raise ValueError(f'Ussage: {sys.argv[0]} [--mac] <message>')
    useMac = False
    message = sys.argv[1]
    if len(sys.argv) == 3:
        useMac = sys.argv[1] == '--mac'
        message = sys.argv[2]

    iv, encryptedMessage = CBC_AES.encrypt(message)
    print('==================== Encrypted ====================')
    print(f'IV:                          {iv}')
    print(f'Encrypted Message:           {encryptedMessage}')

    decryptUrl = 'http://localhost:5000/cbc-aes/mac-decrypt'
    macDecryptUrl = 'http://localhost:5000/cbc-aes/decrypt'
    url = decryptUrl if useMac else macDecryptUrl
    params = { 'iv': iv, 'encryptedMessage': encryptedMessage }
    if useMac:
        macTag = AES_MAC.generateMAC(encryptedMessage)
        params['macTag'] = macTag
        print(f'Message Authentication Code: {macTag}')

    print('========== Sending to Server ==========')
    print(f'Endpoint Url: {url}')
    print(f'Params: {params}')
    response = requests.get(url, params)
    responseText = response.text
    responseCode = response.status_code
    print('========== Server Responding ==========')
    print(f'Status Code: {responseCode}')
    if (responseCode >= 200 and responseCode < 400):
        print(f'Response Data: {responseText}')

if __name__ == "__main__":
    main()