import requests
from requests import get
from bs4 import BeautifulSoup
import helper

tplBaseURL = "https://www.imdb.com/title/%s"
tplSearchURL = "https://www.imdb.com/search/title/?title=%s&release_date=%s-01-01,%s-12-31"
tplAkasBaseURl = "http://www.akas.imdb.com/title/%s"

class IMDB(object):

    def __init__(self):
        self.searchURL = ""
        self.title = ""
        self.movieURL = ""
        self.plotSummary = ""
        self.director = ""
        self.threadTitle = ""
        self.foreignTitle = ""
        self.year = ""
        self.imdbCode = ""
        
    def build(self, blurayTitle, blurayYear, blurayRuntime):
        self.formatSearchURL(blurayTitle, blurayYear)
        self.scrapeIMDBLink(blurayRuntime)
        self.scrapeTitle()
        moviePageSoup = BeautifulSoup(requests.get(self.movieURL).text, 'html.parser')
        self.scrapeYear(moviePageSoup)
        self.scrapeDirector(moviePageSoup)
        self.scrapeForeignTitle(blurayTitle)


        
        ###self.printAttrs()

    def formatSearchURL(self, title, year):
        startYear = int(year)-1
        endYear = int(year)+1
        self.searchURL = tplSearchURL % (helper.urlTransform("+",title),startYear,endYear)

    def scrapeIMDBLink(self, blurayRuntime):
        soup = BeautifulSoup(requests.get(self.searchURL).text, 'html.parser')
        imdbCode = soup.find("div", class_="ribbonize")
        imdbCode2 = soup.find_all("div", class_="lister-item mode-advanced")
        print(imdbCode2)
        #self.imdbCode = imdbCode.attrs['data-tconst']
        #self.movieURL = tplBaseURL % (self.imdbCode)

    def scrapeTitle(self):
        soup = BeautifulSoup(requests.get(self.movieURL+"/plotsummary").text, 'html.parser')
        plotSummarySoup = soup.find("ul", class_="ipl-zebra-list", id="plot-summaries-content")
        self.title = plotSummarySoup.contents[1].contents[1].get_text().strip()

    def scrapeYear(self, soup):
        self.year = soup.find("span", id="titleYear").get_text()[1:-1]
    
    def scrapeDirector(self, soup):
        directorSoup = soup.find("div", class_="credit_summary_item")
        self.director = directorSoup.get_text().split("\n")[2].strip()
    
    def scrapeForeignTitle(self, blurayTitle):
        soup = BeautifulSoup(requests.get(self.movieURL+"/releaseinfo").text, 'html.parser')
        foreignTitleSoup = soup.find("table", class_="ipl-zebra-list akas-table-test-only")
        newTest = foreignTitleSoup.findAll("tr", class_="ipl-zebra-list__item aka-item")

        # for i in newTest:
        #     if i.contents[1].text.strip() == "(original title)":
        #         print(i.contents[1].text.strip())
        #         print(i.contents[3].text.strip())
        #     if i.contents[1].text.strip() == "USA":
        #         print(i.contents[1].text.strip())
        #         print(i.contents[3].text.strip())


    
    def printAttrs(self):
        print(f"IMDB-URL: {self.movieURL}")
        print(f"IMDB-TITLE: {self.title}")
        print(f"IMDB-YEAR: {self.year}")
        print(f"IMDB-DIRECTOR: {self.director}")
        print(f"IMDB-SEARCH-URL: {self.searchURL}")

        print()