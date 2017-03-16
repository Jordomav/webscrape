import requests
from bs4 import BeautifulSoup

file = requests.get("https://github.com/Jordomav/webscrape")

c = file.content

soup = BeautifulSoup(c, 'html.parser')

print(soup.prettify())