from bs4 import BeautifulSoup
import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)




for movie in tr:
    ttl = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    yr = movie.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rt = movie.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    r = ttl + ' - ' + yr + ' ' + ' ' + rt
    print(r)
