import requests

from bs4 import BeautifulSoup 


# scrape https://hojaleaks.com/python and get the titles/headings of the first three
    
url = "https://hojaleaks.com/python"

response = requests.get(url)


print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

titles = soup.find_all('h1')

for title in titles:
    print(title.text)