import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start={}&ref_=adv_nxt"

movies_data = []


def scrape_movies(pages=5):  # pages = number of 50-item pages to scrape
    for page in range(1, pages * 50, 50):
        print(f"Scraping page starting at movie {page}...")
        url = BASE_URL.format(page)
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        movie_containers = soup.find_all("div", class_="lister-item mode-advanced")

        for movie in movie_containers:
            title = movie.h3.a.text if movie.h3.a else None
            year = (
                movie.h3.find("span", class_="lister-item-year").text
                if movie.h3.find("span", class_="lister-item-year")
                else None
            )
            genre = (
                movie.find("span", class_="genre").text.strip()
                if movie.find("span", class_="genre")
                else None
            )
            rating = (
                movie.find("div", class_="inline-block ratings-imdb-rating").strong.text
                if movie.find("div", class_="inline-block ratings-imdb-rating")
                and movie.find("div", class_="inline-block ratings-imdb-rating").strong
                else None
            )
            summary = movie.find_all("p", class_="text-muted")
            description = summary[1].text.strip() if len(summary) > 1 else None

            movies_data.append(
                {
                    "Title": title,
                    "Year": year,
                    "Genre": genre,
                    "Rating": rating,
                    "Description": description,
                }
            )

        time.sleep(1)  # be polite and avoid overloading the server


scrape_movies(pages=20)  # 20 pages → 1,000 movies

# Save to CSV
df = pd.DataFrame(movies_data)
df.to_csv("../scraped_data/imdb_movies.csv", index=False, encoding="utf-8")

print(f"Scraped {len(movies_data)} movies and saved to imdb_movies.csv")
