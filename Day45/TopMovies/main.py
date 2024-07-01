import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movie_list = []

list = soup.find_all(name="h3", class_ = "listicleItem_listicle-item__title__BfenH")

for movie in range(-1, -101, -1):
    movie_list.append(list[movie].text)


with open("./day45/Topmovies/movies.txt", "w") as file:
    for index in range(0,100):
        file.write(f"{movie_list[index]}\n")