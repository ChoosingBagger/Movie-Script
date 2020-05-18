from requests import get
import shutil
import os


class MovieDB(object):

    def __init__(self):
        # Key taken from a special project that is amazing!
        self.api_url = "https://api.themoviedb.org/3/search/movie?api_key=b8eabaf5608b88d0298aa189dd90bf00"
        self.poster_url = "https://image.tmdb.org/t/p/original"

    def build(self, title, year):
        self.definite = False
        self.title = title[3]
        for entry in title:
            search_url = f"{self.api_url}&language=en-US&query={entry}&page=1&include_adult=false&year={year}"
            r = get(url=search_url)
            self.tmdbSearch = r.json()
            self.scrapeURL(entry, year)
            self.truthURL()
        self.grabPoster(self.title)

    def scrapeURL(self, title, year):
        try:
            for result in self.tmdbSearch["results"]:
                if self.tmdbSearch["total_results"] == 1:
                    self.scrapeLogic(result)
                    self.definite = True

                elif result["original_title"] == title:
                    self.scrapeLogic(result)
                    self.probable = True

                elif result["title"] == title:
                    self.scrapeLogic(result)
                    self.maybe = True
        except KeyError:
            pass

    def scrapeLogic(self, result):
        movie_id = result["id"]
        self.tempURL = f"https://themoviedb.org/movie/{movie_id}"
        self.tempPoster = result["poster_path"]
        year = result["release_date"].split("-", 1)[0][-4:]
        self.tempYear = year

    def truthURL(self):
        # Iterates through the scrapeURL logic, picks best one and assigns
        # each as the truth of their respective pieces.
        try:
            if self.definite:
                self.truthLogic()
            elif self.probable and not self.definite:
                self.truthLogic()
            elif self.maybe and not self.definite and not self.probable:
                self.truthLogic()
        except AttributeError:
            pass

    def truthLogic(self):
        self.url = self.tempURL
        self.poster = self.tempPoster
        self.year = self.tempYear

    def grabPoster(self, title):
        resp = get(self.poster, stream=True)
        fileName = title + '.jpg'
        localFile = open(fileName, 'wb')

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True

        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, localFile)
        fullPath = os.path.abspath(localFile)
        self.posterPath = fullPath
