from datetime import datetime

def logMessage(message):
    with open('messages.log', 'w') as f:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f.write(f'{now}|{message}')