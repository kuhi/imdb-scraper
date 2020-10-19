from bs4 import BeautifulSoup

from imdb.utils import get_imdb_data


class ImdbMovieEntry:
    """
    A simple class for storing IMDB Movie entries.
    """

    def __init__(self, element):
        self.title = self.extract_title(element)
        self.rating = self.extract_rating(element)
        self.extra_info = self.extract_extra_info(element)

    def get_extra_info(self):
        return self.extra_info

    def get_title(self):
        return self.title

    def get_rating(self):
        return self.rating

    def __str__(self):
        return self.title

    def get_extra_info_str(self):
        extra_info = [f"{k}: {v}" for k, v in self.extra_info.items()]
        return f"{', '.join(extra_info)}"

    @staticmethod
    def extract_title(element):
        title = element.find('td', {'class': 'titleColumn'}).find('a').contents[0]
        return title

    @staticmethod
    def extract_rating(element):
        rating = element.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
        return rating

    @staticmethod
    def extract_extra_info(element):
        # TODO get director, runtime, year
        extra_info = dict()
        # First, we need the url to the movie page
        url = element.find("td", {"class": "titleColumn"}).find("a").find(attrs="href").contents[0]["value"]
        full_url = f"https://www.imdb.com/{url}"
        response = get_imdb_data(full_url)
        soup = BeautifulSoup(response)
        # Get the movie's header, or its 'title'
        title_subtext = soup.find("div", id="title-overview-widget").find("div", {"class": "subtext"}).contents[0]

        return extra_info
