import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.uol.com.br')
soup = BeautifulSoup(r.content)
news = []
for item in soup.find_all('h2',{'class': 'titulo color2'}):
  news.appned(item.text)
news
