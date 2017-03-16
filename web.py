import requests
from bs4 import BeautifulSoup

file = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

c = file.content

soup = BeautifulSoup(c, 'html.parser')

# Get all links on the page of they are https
def get_first_link():
    for link in soup.find_all('a'):
        if "https" in str(link):
            return link.get('href')

source = requests.get(get_first_link()).content

py_soup = BeautifulSoup(source, 'html.parser')

print(py_soup.prettify())