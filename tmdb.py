from requests import get


class MovieDB(object):

    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/search/movie?api_key=b8eabaf5608b88d0298aa189dd90bf00"

    def build(self, title, year):
        self.definiteURL = False
        for entry in title:
            search_url = f"{self.api_url}&language=en-US&query={entry}&page=1&include_adult=false&year={year}"
            r = get(url=search_url)
            self.tmdbSearch = r.json()
            self.scrapeURL(entry, year)
            self.truthURL()
        print(title[3])
        print(self.url)

    def scrapeURL(self, title, year):
        try:
            for results in self.tmdbSearch["results"]:
                if self.tmdbSearch["total_results"] == 1:
                    movie_id = results["id"]
                    self.definiteURL = f"https://themoviedb.org/movie/{movie_id}"

                elif results["original_title"] == title:
                    movie_id = results["id"]
                    self.probableURL = f"https://themoviedb.org/movie/{movie_id}"

                elif results["title"] == title:
                    movie_id = results["id"]
                    self.maybeURL = f"https://themoviedb.org/movie/{movie_id}"
        except KeyError:
            pass

    def truthURL(self):
        try:
            if self.definiteURL:
                self.url = self.definiteURL
            elif self.probableURL and not self.definiteURL:
                self.url = self.probableURL
            elif self.maybeURL and not self.definiteURL and not self.probableURL:
                self.url = self.maybeURL
        except AttributeError:
            pass
