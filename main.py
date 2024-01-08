import requests, threading

url = input('Enter your URL: ')
threads = input('Enter the amount of threads:  ')

sent = 0

def thread():
  global url
  global sent
  while True:  
     r = requests.get(url)
     if not r.ok:
         print('Failed to request URL.')
     else:
       sent += 1
       print(f'Successfully sent a request to {url}. ({str(sent)})')

for _ in range(int(threads)):
    t = threading.Thread(target=thread)
    t.start()
