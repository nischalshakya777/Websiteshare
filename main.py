from bs4 import BeautifulSoup
import requests
import lxml
from csv import writer
from csv import DictWriter
import os

# Site URL
url = "https://www.sharesansar.com/market"

# make a Get request to fentch the raw HTML data
con = requests.get(url)
soup = BeautifulSoup(con.text, 'lxml')  # code of the page

table = soup.find('table', class_="table table-bordered table-striped table-hover")  # table of data
headers = [i.text for i in table.find_all('th')]  # data of the th tag

with open('index.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers)
    f_object.close()
data = [j.text for j in table.find_all('td')]  # data inside the tr tag
i = 0
while i < 13:
    dict = {'Index': data[i], 'Close': data[i + 1], 'Point Change': data[i + 2],
            '% Change': data[i + 3]}
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
i = 0
while i < 65:
    dict = {'Sub-Indices': data1[i], 'Turnover': data1[i + 1], 'Close': data1[i + 2], 'Point': data1[i+3],
            '% Change': data1[1+4]}
    with open('Sub-Indices.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=head)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 5
print(headers)
print(data)
print(head)
print(data1)
#change location if file in different location
os.system('python ../pythonProject3/Nepse.py')
