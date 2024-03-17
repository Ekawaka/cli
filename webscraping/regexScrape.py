import requests
import re
from bs4 import BeautifulSoup

url = "https://zinduaschool.com/2024-hackathons-to-watch-out-for/ lorem dsfbkjsdjkf, sdfjbsdkf, https://test.com"

response = requests.get(url)
print(response.content)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

phone_pattern = r"\(\+?d{3}\)?(0)[-.\s]?\d{3}[]"

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

urls = re.findall(url_pattern, str(soup))

for url in urls:
    print(urls)

