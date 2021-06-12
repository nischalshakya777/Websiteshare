from bs4 import BeautifulSoup

import requests

import csv

csv_file = open('nepse.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow('s')

for i in range(1, 12):
    url = ["http://www.nepalstock.com/main/todays_price/index/1/",  # for Nepse market data
           "http://www.nepalstock.com/main/todays_price/index/2/",
           "http://www.nepalstock.com/main/todays_price/index/3/",
           "http://www.nepalstock.com/main/todays_price/index/4/",
           "http://www.nepalstock.com/main/todays_price/index/5/",
           "http://www.nepalstock.com/main/todays_price/index/6/",
           "http://www.nepalstock.com/main/todays_price/index/7/",
           "http://www.nepalstock.com/main/todays_price/index/8/",
           "http://www.nepalstock.com/main/todays_price/index/9/",
           "http://www.nepalstock.com/main/todays_price/index/10/",
           "http://www.nepalstock.com/main/todays_price/index/11/"]
    print(url[i - 1])
    u = url[i - 1]
    source = requests.get(u)
    soup = BeautifulSoup(source.text, 'lxml')
    contain = soup.find('div', class_='container')
    data = contain.find_next('tr', class_='unique').find_all_next('td')
    csv_file = open('nepse.csv', 'a')
    csv_writer = csv.writer(csv_file)
    for d in data:
        print(d.text)
        csv_writer.writerow([d.text])

url = "http://www.nepalstock.com/"
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
data = soup.find_all('table', class_='table table-hover table-condensed')
csv_file = open('nepsemainpage.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow('s')

for d in data:
    raw = d.find_all('td')
    for r in raw:
        l = r.find_all('img')
        csv_file = open('nepsemainpage.csv', 'a')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([r.text])
        print(r.text)
