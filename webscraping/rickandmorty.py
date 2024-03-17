# fetch the following data from the rick and morty API:
# - 20 characters
# - 20 locations 
# - 20 episodes
#  and save it in a CSV file

import requests
import csv

url = "https://rickandmortyapi.com/"

response = requests.get(url)
print(response)


