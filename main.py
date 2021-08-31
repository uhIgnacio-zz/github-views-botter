import requests, threading

url = input('raw link: ')
amount = input('enter the amount of threads (go for 300): ')
sent = 0

def thread():
  global sent
  while True:    
      requests.get(url)
      sent += 1
      print(f'Views sent: %s' % sent)

for _ in range(int(amount)):
    t = threading.Thread(target=thread)
    t.start()
