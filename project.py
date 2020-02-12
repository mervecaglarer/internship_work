import lxml.html as parser
import requests
import csv

header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

url = "https://www.hepsiburada.com/apple-iphone-6s-16-gb-apple-turkiye-garantili-p-TELCEPIPH6S16SI-N"
response = requests.get(url, headers=header)

file = csv.writer(open("properties.csv", "w"))

if response.status_code == 200:
    parsed = parser.document_fromstring(response.text)
    table = parsed.get_element_by_id("productTechSpecContainer").findall("table")[1]
    rows = table.findall('tbody')[0].findall('tr')
    for row in rows:
        feature = row.findall('th')[0].text_content()
        value = row.findall('td')[0].text_content()
        file.writerow([feature, value])
    table = parsed.get_element_by_id("productTechSpecContainer").findall("table")[2]
    rows = table.findall('tbody')[0].findall('tr')
    for row in rows:
        feature = row.findall('th')[0].text_content()
        value = row.findall('td')[0].text_content()
        file.writerow([feature, value])
