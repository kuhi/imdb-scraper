from bs4 import BeautifulSoup
import requests

from imdb.movie import ImdbMovieEntry


def process_chart(response, top=10):
    soup = BeautifulSoup(response)
    titles = list()
    movies_iter = iter(soup.findChildren("tr"))
    counter = 0

    skip_first = next(movies_iter, None)
    # Skipping the table's header
    if skip_first is not None:
        movie_element = next(movies_iter, None)
        while movie_element is not None or counter < top:
            movie_entry = ImdbMovieEntry(movie_element)
            titles.append(movie_entry)
            counter += 1
            movie_element = next(movies_iter, None)
    return titles


def get_imdb_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
