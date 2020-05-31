from requests import get
from bs4 import BeautifulSoup


class Bluray(object):

    # intializes the bluray object, sets the blurayURL
    def __init__(self, movieURL):
        self.movieURL = movieURL
        self.title = ""
        self.country = ""
        self.movieDistributor = ""
        self.year = ""
        self.runtime = 0
        self.imdbLink = ""
        self.rtLink = ""

    def build(self):
        soup = BeautifulSoup(get(self.movieURL).text, 'html.parser')
        self.scrapeTitle(soup)
        self.scrapeCountry(soup)
        self.scrapeMovieDistributor(soup)
        self.scrapeYear(soup)
        self.scrapeRuntime(soup)
        self.scrapeIMDBLink(soup)
        self.scrapeRTLink(soup)
        #self.printAttrs()

    def scrapeTitle(self, soup):
        titleRaw = soup.find("div", id="movie_info")
        self.title = titleRaw.contents[1].get_text()

    def scrapeCountry(self, soup):
        countryRaw = soup.find("a", class_="black noline")
        self.country = countryRaw.next_sibling.get("title").title()

    def scrapeMovieDistributor(self, soup):
        movieInfoRaw = soup.find("span", class_="subheading grey")
        self.movieDistributor = movieInfoRaw.get_text().split("|")[0].strip()

    def scrapeYear(self, soup):
        movieInfoRaw = soup.find("span", class_="subheading grey")
        self.year = movieInfoRaw.get_text().split("|")[1].strip()

    def scrapeRuntime(self, soup):
        movieInfoRaw = soup.find("span", class_="subheading grey")
        self.runtime = int(movieInfoRaw.get_text().split("|")[2].strip().split(" ")[0].strip())

    def scrapeIMDBLink(self, soup):
        self.imdbLink = soup.find("a", id="imdb_icon").attrs['href']

    def scrapeRTLink(self, soup):
        self.rtLink = soup.find("a", id="rt_icon").attrs['href']

    def printAttrs(self):
        print(f"BLURAY-TITLE: {self.title}")
        print(f"BLURAY-COUNTRY: {self.country}")
        print(f"BLURAY-DISTRIBUTOR: {self.movieDistributor}")
        print(f"BLURAY-YEAR: {self.year}")
        print(f"BLURAY-RUNTIME: {self.runtime}")
        print(f"IMDB-LINK: {self.imdbLink}")
        print(f"RT-LINK: {self.rtLink}")
        print()
