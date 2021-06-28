from bs4 import BeautifulSoup
import requests
import lxml
from csv import writer
from csv import DictWriter

# Site URL
url = "http://www.nepalstock.com/gainers"
url1 = "http://www.nepalstock.com/losers"
url2 = "http://www.nepalstock.com/turnovers"
url3 = "http://www.nepalstock.com.np/"

# make a Get request to fetch the raw HTML data
con = requests.get(url)
soup = BeautifulSoup(con.text, 'lxml')  # code of the page
table = soup.find('table', attrs={'class': 'dataTable table'})
con1 = requests.get(url1)
soup1 = BeautifulSoup(con1.text, 'lxml')  # code of the page
table1 = soup1.find('table', attrs={'class': 'dataTable table'})
con2 = requests.get(url2)
soup2 = BeautifulSoup(con2.text, 'lxml')  # code of the page
table2 = soup2.find('table', attrs={'class': 'dataTable table'})
con3 = requests.get(url3)
soup3 = BeautifulSoup(con3.text, 'lxml')  # code of the page
table3 = soup3.find_all('table', attrs={'class': 'table table-hover table-condensed'})[3]

# Gainer
head = table.find('tr', class_="rowtitle1")
headers = [i.text for i in head.find_all('td')]  # data of the th tag

with open('gainer.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers)
    f_object.close()
data = [j.text for j in table.find_all('td')[4:]]
data = [item.replace(',', '') for item in data if str(item)]
data = [item.replace(' ', '') for item in data if str(item)]
i = 0
while i < len(data):
    dict = {headers[0]: data[i], headers[1]: data[i + 1], headers[2]: data[i + 2]}
    with open('gainer.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 3

# Loser
with open('loser.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers)
    f_object.close()
data1 = [j.text for j in table1.find_all('td')[4:]]
data1 = [item.replace(',', '') for item in data1 if str(item)]
data1 = [item.replace(' ', '') for item in data1 if str(item)]
i = 0
while i < len(data1):
    dict = {headers[0]: data1[i], headers[1]: data1[i + 1], headers[2]: data1[i + 2]}
    with open('loser.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 3

# Turnover
head2 = table2.find('tr', class_="rowtitle1")
headers2 = [i.text for i in head2.find_all('td')]  # data of the td tag
with open('Top10Turnover.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers2)
    f_object.close()
data2 = [j.text for j in table2.find_all('td')[5:]]
data2 = [item.replace(',', '') for item in data2 if str(item)]
data2 = [item.replace(' ', '') for item in data2 if str(item)]
i = 0
while i < 30:
    dict = {headers2[0]: data2[i], headers2[1]: data2[i + 1], headers2[2]: data2[i + 2]}
    with open('Top10Turnover.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers2)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 3

# Market Summary
data3 = [i.text for i in table3.find_all('td')][1:]
data3 = [item.strip() for item in data3 if str(item)]
data3 = [item.replace(',', '') for item in data3 if str(item)]
data3 = [item.replace(' ', '') for item in data3 if str(item)]
head3 = ['Market Summary', 'Data']
with open('Market_Summary.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(head3)
    f_object.close()
i = 0
while i < len(data3):
    dict = {'Market Summary': data3[i], 'Data': data3[i + 1]}
    with open('Market_Summary.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=head3)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 2

# Print DAta
