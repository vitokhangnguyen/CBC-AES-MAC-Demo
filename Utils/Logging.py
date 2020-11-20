from datetime import datetime

def logMessage(message, useMac=False):
    with open('messages.log', 'a') as f:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if useMac:
            f.write(f'{now} | {message} | with MAC\n')
        else:
            f.write(f'{now} | {message}\n')