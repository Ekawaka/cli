import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

articles = soup.find_all('article', class_='css-8atqhb')
data = []

for article in articles[:10]:
    title = article.find('h2', class_='css-1vvhd4r').text.strip()
    description = article.find('p', class_='css-1echdzn').text.strip()
    data.append({'title': title, 'description': description})
    print(article.text)

with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)