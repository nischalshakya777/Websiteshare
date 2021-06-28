from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
from csv import writer
from csv import DictWriter

import os

# Site URL
url = "https://www.sharesansar.com/market"

# make a Get request to fetch the raw HTML data
con = requests.get(url)
soup = BeautifulSoup(con.text, 'lxml')  # code of the page

table = soup.find('table', class_="table table-bordered table-striped table-hover")  # table of data
headers = [i.text for i in table.find_all('th')]  # data of the th tag

with open('index.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers)
    f_object.close()
data = [j.text for j in table.find_all('td')]
data = [item.replace(',', '') for item in data if str(item)]
data = [item.strip() for item in data if str(item)]
data = [item.replace(' ', '') for item in data if str(item)]

i = 0
while i < len(data):
    dict = {headers[0]: data[i], headers[1]: data[i + 1], headers[2]: data[i + 2],
            headers[3]: data[i + 3]}
    with open('index.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 4

os.system('python ../pythonProject3/Nepse.py')
table1 = soup.find_all('th')[25:-21]
head = [i.text for i in table1]
with open('Sub-Indices.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(head)
    f_object.close()
table2 = soup.find_all('td')[28:-122]
data1 = [j.text for j in table2]
data1 = [item.strip() for item in data1 if str(item)]
data1 = [item.replace(',', '') for item in data1 if str(item)]
data1 = [item.replace(' ', '') for item in data1 if str(item)]

i = 0
while i < 65:
    dict = {head[0]: data1[i], head[1]: data1[i + 1], head[2]: data1[i + 2], head[3]: data1[i + 3],
            head[4]: data1[i + 4]}
    with open('Sub-Indices.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=head)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 5

os.system('python ../pythonProject3/Nepse.py')
