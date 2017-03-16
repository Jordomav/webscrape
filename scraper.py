import sample

sample.init()

from bs4 import BeautifulSoup
soup = BeautifulSoup(sample.html_doc, 'html.parser')

print(soup.prettify())