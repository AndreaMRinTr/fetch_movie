import requests
import re
import csv
from bs4 import BeautifulSoup


class IMDBScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape_movies_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')

        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

        movies_data = []
        for index in range(0, len(movies)):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index + 1)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index + 1)) - (len(movie) - len(str(index + 1)))]

            data = {"movie_id": index + 1,
                    "movie_title": movie_title,
                    "movie_rating": ratings[index],
                    "movie_year": year,
                    "movie_genre": "",
                    "star_cast": crew[index],
                    "vote": votes[index],
                    "link": f'http://www.imdb.com{links[index]}'
                    }
            movies_data.append(data)

        return movies_data


class Movie:
    def __init__(self, movie_id, movie_title, movie_rating, movie_year, movie_genre, star_cast, vote, link):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.movie_rating = movie_rating
        self.movie_year = movie_year
        self.movie_genre = movie_genre
        self.star_cast = star_cast
        self.vote = vote
        self.link = link


class MovieDataWriter:
    def __init__(self, filename, fields):
        self.filename = filename
        self.fields = fields
    
    def write_movies_data_to_csv(self, movies_data):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            for movie_data in movies_data:
                movie = Movie(**movie_data)
                writer.writerow({
                    "movie_id": movie.movie_id,
                    "movie_title": movie.movie_title,
                    "movie_rating": movie.movie_rating,
                    "movie_year": movie.movie_year,
                    "movie_genre": movie.movie_genre,
                    "star_cast": movie.star_cast,
                    "vote": movie.vote,
                    "link": movie.link
                })


def main():
    url = 'http://www.imdb.com/chart/top'
    scraper = IMDBScraper(url)
    movies_data = scraper.scrape_movies_data()

    fields = ["movie_id", "movie_title", "movie_rating", "movie_year", "movie_genre", "star_cast", "vote", "link"]
    writer = MovieDataWriter("movie_results.csv", fields)
    writer.write_movies_data_to_csv(movies_data)


if __name__ == '__main__':
    main()
