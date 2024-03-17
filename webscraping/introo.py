import requests
from bs4 import BeautifulSoup 
import csv

url = "https://hojaleaks.com"



response = requests.get(url)

print(response.status_code)

print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    print(paragraph.text)

# scrape https://hojaleaks.com/python and get the titles/headings of the first three
    
with open("info.csv", 'w') as file:
    writer = csv.writer(file)
    for paragraph in paragraphs:
        writer.writerow(paragraph)
