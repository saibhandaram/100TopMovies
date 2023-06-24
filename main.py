import requests as requests
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.h3)
all_titles = soup.find_all('h3')
new_title = all_titles[::-1]
for title in new_title:
    print(title.getText())

with open('movies.txt', mode='w', encoding='utf-8') as movies_file:
    for movie in new_title:
        movies_file.write(f"{movie.getText()}\n")
