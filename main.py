import requests, threading, os

url = os.environ['URL']
amount = os.environ['AMOUNT']

def thread():
  sent = 0
  while True:    
      requests.get(url)
      sent += 1
      print(f'Views sent: %s' % sent)

for _ in range(int(amount)):
    t = threading.Thread(target=thread)
    t.start()
