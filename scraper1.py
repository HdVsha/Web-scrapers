from requests import get
from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
from re import sub
import pandas as pd
import csv


if __name__ == "__main__":
    URL = 'https://codeforces.com/contests'
    page = get(URL)
    # or uClient = uReq(URL), uClient.read()
    soup = BeautifulSoup(page.content, 'html.parser')  # parsing the website
    containers = soup.find_all('tr')
    info = []
    for container in containers:
        tds = container.find_all('td')
        tmp_array = []
        for td in tds:
            tmp_array.append(sub(r'\s+|(Enter » Virtual participation »)', ' ', td.text))
        info.append(tmp_array)

    header = ["NAMES", "AUTHORS", "START", "DURATION", " ", " "]

    df = pd.DataFrame(info, columns=header)
    df.to_csv('tmp_file.csv', sep='\t', na_rep='Unkown')  # or below

    # with open("tmp_file.csv", "w") as f:
    #     writer = csv.writer(f, delimiter=',')
    #     writer.writerow(header)
    #     for line in info:
    #         writer.writerow([elem for elem in line])
