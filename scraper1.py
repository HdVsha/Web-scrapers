import requests
import bs4  # or from bs4(BeautifulSoup4) import BeautifulSoup
from urllib.request import urlopen as uReq
import re

URL = 'https://codeforces.com/contests'
page = requests.get(URL)
# or uClient = uReq(URL), uClient.read()
soup = bs4.BeautifulSoup(page.content, 'html.parser')  # parsing the website  # or soup.find('body') --- will print all the content
containers = soup.find_all('tr')
info = []
for container in containers:
    tds = container.find_all('td')
    for td in tds:
        info.append(re.sub(r'\s+',' ',td.text))

print(info)


