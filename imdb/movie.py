import logging
from bs4 import BeautifulSoup
import re

from imdb import utils

logging.basicConfig(level=logging.INFO)


class ImdbMovieEntry:
    """
    A simple class for storing IMDB Movie entries.
    """

    def __init__(self, element: BeautifulSoup, extra_info: bool = False):
        self.title = self.extract_title(element)
        self.rating = self.extract_rating(element)
        self.extra_info = self.extract_extra_info(element) if extra_info else dict()

    def get_extra_info(self) -> dict:
        return self.extra_info

    def get_title(self) -> str:
        return self.title

    def get_rating(self) -> float:
        return self.rating

    def __str__(self):
        return self.title

    def to_dict(self, extra_info: bool = False) -> dict:
        movie_dict = {"title": self.title, "rating": self.rating}
        if extra_info:
            movie_dict = {**movie_dict, **self.extra_info}
        return movie_dict

    def get_extra_info_str(self) -> str:
        extra_info = [f"{k}: {v}" for k, v in self.extra_info.items()]
        return f"{', '.join(extra_info)}"

    @staticmethod
    def extract_title(element: BeautifulSoup) -> str:
        title = element.find("td", {"class": "titleColumn"}).find("a").contents[0]
        return title

    @staticmethod
    def extract_rating(element: BeautifulSoup) -> float:
        rating = float(
            element.find("td", {"class": "ratingColumn imdbRating"})
            .find("strong")
            .contents[0]
        )
        return rating

    @staticmethod
    def extract_extra_info(element: BeautifulSoup) -> dict:
        extra_info = dict()
        # First, we need the url to the movie page
        url = element.find("td", {"class": "titleColumn"}).find("a").attrs.get("href")
        if url:
            full_url = f"https://www.imdb.com/{url}"
            response = utils.get_imdb_data(full_url)
            soup = BeautifulSoup(response, features="html.parser")
            # Get the movie's header, or its 'title'
            title_subtext = soup.find("div", id="title-overview-widget").find(
                "div", {"class": "subtext"}
            )

            time = title_subtext.find("time").contents[0].strip()
            genre_regex = re.compile("^.+genres$")
            genres = ",".join(
                [
                    str(genre.contents[0])
                    for genre in title_subtext.findAll("a")
                    if genre_regex.match(genre.attrs["href"])
                ]
            )
            released = [
                str(released.contents[0])
                for released in title_subtext.findAll("a")
                if "title" in released.attrs
                and released.attrs["title"] == "See more release dates"
            ][0].strip()

            extra_info = {
                "time": time,
                "genre(s)": genres,
                "released": released,
            }
        return extra_info
