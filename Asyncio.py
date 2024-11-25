import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

titles = [i['alt'] for i in soup.find_all('img')]
prices = [i.text[1:] for i in soup.find_all('p', {'class': 'price_color'})]
stocks = [i.text.strip() for i in soup.find_all('p', {'class': 'instock availability'})]
photos = [i['src'] for i in soup.find_all('img')]
text = ''


for t in range(len(titles)):
    text += f'{titles[t]}\n{prices[t]}\n{stocks[t]}\n{photos[t]}\n                                                      \n'


print(text)

