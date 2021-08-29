import requests

url = input('raw link: ')
sent = 0

while True: 
    requests.get(url)
    sent += 1
    print(f'Views sent: %s' % sent)