#Write a program to scrape the titles and descriptions of the top 10 articles from the front page of the
# New York Times (https://www.nytimes.com/) and store them in a CSV file.

import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.nytimes.com/"

response = requests.get(url)

print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

