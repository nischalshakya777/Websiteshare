from bs4 import BeautifulSoup
import requests
import lxml
import csv

url = "https://merolagani.com/LatestMarket.aspx"

con = requests.get(url)
soup = BeautifulSoup(con.text, 'lxml')
table = soup.find('table', class_="table table-hover live-trading sortable")
headers = [i.text for i in table.find_all('th')]
data = [j for j in table.find_all('tr', {"class": ["decrease-row", "increase-row", "no-change-row"]})]
result = [{headers[index]: cell.text for index, cell in enumerate(row.find_all("td"))} for row in data]
print(result)
csv_file = open('nepse.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(result)
