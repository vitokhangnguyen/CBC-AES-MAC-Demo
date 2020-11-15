import sys
import requests
import CBC_AES

def main():
    if (len(sys.argv) != 2):
        raise ValueError(f'Ussage: {sys.argv[0]} <message>')
    message = sys.argv[1]
    iv, encryptedMessage = CBC_AES.encrypt(message)
    print('========== Encrypted ==========')
    print(f'IV:                {iv}')
    print(f'Encrypted message: {encryptedMessage}')

    print('========== Sending to Server ==========')
    url = 'http://localhost:5000/cbc-aes/decrypt'
    params = { 'iv': iv, 'encryptedMessage': encryptedMessage }
    print(f'Endpoint Url: {url}')
    print(f'Params: {params}')
    response = requests.get(url, params)
    responseText = response.text
    print('========== Server Responding ==========')
    print(responseText)

if __name__ == "__main__":
    main()