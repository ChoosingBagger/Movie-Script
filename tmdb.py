from requests import get
import shutil


class MovieDB(object):

    def __init__(self):
        # Key taken from a special project that is amazing!
        self.api_url = ""
        self.title = ""
        self.tmdbSearch = ""
        self.tmdbResult = ""
        self.url = ""
        self.poster = ""
        self.year = ""
        self.posterPath = ""

    def build(self, imdbID, folder):
        imdbID = imdbID.split("/tt")
        imdbID = "tt" + imdbID[1].replace("/", "")
        self.api_url = f"https://api.themoviedb.org/3/find/{imdbID}?api_key=b8eabaf5608b88d0298aa189dd90bf00&language=en-US&external_source=imdb_id"
        search_url = f"{self.api_url}&language=en-US&external_source=imdb_id"
        r = get(url=search_url)
        self.tmdbSearch = r.json()
        self.scrapeLogic()
        self.grabPoster(folder)

    def scrapeLogic(self):
        try:
            self.tmdbResult = self.tmdbSearch["movie_results"][0]
            self.title = self.tmdbResult["title"]
            self.year = self.tmdbResult["release_date"].split("-", 1)[0][-4:]
        except KeyError:
            try:
                self.tmdbResult = self.tmdbSearch["tv_results"][0]
                self.title = self.tmdbResult["original_name"]
                self.year = self.tmdbResult["first_air_date"].split("-", 1)[0][-4:]
            except KeyError:
                try:
                    self.tmdbResult = self.tmdbSearch["tv_season_results"][0]
                    self.title = self.tmdbResult["original_name"]
                except KeyError:
                    print("tmdb no worky")
                    pass
        self.tmdbID = self.tmdbResult["id"]
        self.url = f"https://themoviedb.org/movie/{self.tmdbID}"
        poster_path = self.tmdbResult["poster_path"]
        self.poster = f"https://image.tmdb.org/t/p/original{poster_path}"

    def grabPoster(self, folder):
        resp = get(self.poster, stream=True)
        fileName = "poster.jpg"
        fileName = folder / fileName
        localFile = open(fileName, 'wb')

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True

        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, localFile)
        self.posterPath = fileName

    def printAttrs(self):
        print(f"TMDB-TITLE: {self.title}")
        print(f"TMDB-POSTERURL: {self.poster}")
        print(f"TMDB-POSTERPATH: {self.posterPath}")
        print(f"TMDB-YEAR: {self.year}")
        print()
