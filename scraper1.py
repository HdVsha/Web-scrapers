from requests import get
from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
from re import sub


if __name__ == "__main__":
    URL = 'https://codeforces.com/contests'
    page = get(URL)
    # or uClient = uReq(URL), uClient.read()
    soup = BeautifulSoup(page.content, 'html.parser')  # parsing the website
    containers = soup.find_all('tr')
    info = []
    for container in containers:
        tds = container.find_all('td')
        for td in tds:
            info.append(sub(r'\s+',' ',td.text))

    print(info)
