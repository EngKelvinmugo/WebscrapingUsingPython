import requests
from bs4 import BeautifulSoup


req = requests.get("https://myportfolio.kelvinmugo.repl.co/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())