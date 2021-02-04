from requests import get
from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
from re import sub
import pandas as pd
# import csv
import scrapy


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

    '''
    ALARM!!! In order to run the code below you need to put this "spider" into 'spiders' dir in your Scrapy project
    and run 'scrapy crawl cf_contests -o contests.json' in your terminal to save the info from the site
    (and do not forget to change 'ROBOTSTXT_OBEY = True' --> 'ROBOTSTXT_OBEY = False' in settings.py
    '''
    class CFContests(scrapy.spiders.Spider):
        name = "cf_contests"

        start_urls = [
            "https://codeforces.com/contests/"
        ]

        def parse(self, response):
            yield {
                # css parser
                'Name of the contest': response.css('div.contests-table div.datatable table tr td::text').getall(),
                # [href*=profile] --- checks whether the 'profile' is in the URL
                'Bosses': response.css('div.contests-table div.datatable table tr a[href*=profile]::text').getall()
            }

