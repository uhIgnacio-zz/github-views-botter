import requests, threading, os

url = input('raw link: ')
amount = input('enter the amount of threads (go for 300): ')

def thread():
  while True:  
     sent = 0
     r = requests.get(url)
     if r.status_code == 403:
         print('Invalid URL')
     else:
      pass
      sent += 1
      print(f'Views sent: %s' % sent)

for _ in range(int(amount)):
    t = threading.Thread(target=thread)
    t.start()
