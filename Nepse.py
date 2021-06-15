from bs4 import BeautifulSoup
import requests
import lxml
from csv import writer
from csv import DictWriter

# Site URL
url = "http://www.nepalstock.com/gainers"
url1 = "http://www.nepalstock.com/losers"
url2 = "http://www.nepalstock.com/turnovers"

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

# Gainer
head = table.find('tr', class_="rowtitle1")
headers = [i.text for i in head.find_all('td')]  # data of the th tag

with open('gainer.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers)
    f_object.close()
data = [j.text for j in table.find_all('td')[4:]]
i = 0
while i < 150:
    dict = {'Symbol': data[i], 'LTP': data[i + 1], '% Change': data[i + 2]}
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
i = 0
while i < 150:
    dict = {'Symbol': data1[i], 'LTP': data1[i + 1], '% Change': data1[i + 2]}
    with open('loser.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 3

# Turnover
head2 = table2.find('tr', class_="rowtitle1")
headers2 = [i.text for i in head2.find_all('td')]  # data of the th tag
with open('Top10Turnover.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(headers2)
    f_object.close()
data2 = [j.text for j in table2.find_all('td')[5:]]
i = 0
while i < 30:
    dict = {'Symbol': data2[i], 'Turn Over': data2[i + 1], ' Closing Price': data2[i + 2]}
    with open('Top10Turnover.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headers2)
        dictwriter_object.writerow(dict)
        f_object.close()
    i += 3

# Print DAta
print(headers)
print(data)
print(data1)
print(headers2)
print(data2)
