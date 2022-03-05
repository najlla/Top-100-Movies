import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies_title = [movie.getText() for movie in all_movies]
# for n in range(len(movies_title) -1, -1, -1):
#     movies = movies_title[n]

movies = movies_title[::-1]

with open("movies.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

