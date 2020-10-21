from typing import List

from bs4 import BeautifulSoup
import logging
import pandas as pd
import requests

from imdb import movie

logging.basicConfig(level=logging.INFO)


def process_chart(response: str, top: int = 10) -> List[movie.ImdbMovieEntry]:
    logging.info("Processing HTML page.")
    soup = BeautifulSoup(response, features="html.parser")
    titles = list()
    movies_iter = iter(soup.findChildren("tr"))
    counter = 0

    skip_first = next(movies_iter, None)
    # Skipping the table's header
    if skip_first is not None:
        movie_element = next(movies_iter, None)
        while movie_element is not None and counter < top:
            movie_entry = movie.ImdbMovieEntry(movie_element)
            logging.info(f"ImdbMovieEntry: {str(movie_entry)}")
            titles.append(movie_entry)
            counter += 1
            movie_element = next(movies_iter, None)

    logging.info("Done.")
    return titles


def get_imdb_data(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_pandas_dataframe(
    movies_list: List[movie.ImdbMovieEntry],
    extra_info: bool = False,
    min_rating: float = 0,
) -> pd.DataFrame:
    logging.info("Converting list of ImdbMovieEntry into a pandas DataFrame.")

    # Transform list of movies into a DataFrame with the index being all the information about given movie
    df = pd.DataFrame(
        [movie.to_dict(extra_info) for movie in movies_list],
        index=list(movies_list[0].to_dict(extra_info).keys()).remove("rating"),
    )
    # Remove all movies with a rating lower than `min_rating`
    df.drop(df[df["rating"] < min_rating].index, inplace=True)
    df.sort_values("rating", inplace=True)

    logging.info("Done.")
    return df
