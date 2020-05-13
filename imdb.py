import requests
from requests import get
from bs4 import BeautifulSoup
import helper

tplBaseURL = "https://www.imdb.com/title/%s"
tplSearchURL = "https://www.imdb.com/search/title/?title=%s&release_date=%s-01-01,%s-12-31"
tplAkasBaseURl = "http://www.akas.imdb.com/title/%s"
tplForeignBodyTitle = "%s (AKA: %s)"
tplNonForeignBodyTitle = "%s"


class IMDB(object):

    def __init__(self):
        self.searchURL = ""
        self.title = ""
        self.movieURL = ""
        self.plotSummary = ""
        self.director = ""
        self.bodyTitle = ""
        self.foreignTitle = ""
        self.year = ""
        self.imdbCode = ""
        self.usaTitle = ""
        self.worldTitle = ""
        
    def build(self, blurayTitle, blurayYear, blurayRuntime):
        self.formatSearchURL(blurayTitle, blurayYear)
        self.scrapeIMDBLink(blurayRuntime)
        self.scrapePlotSummary()
        moviePageSoup = BeautifulSoup(requests.get(self.movieURL).text, 'html.parser')
        self.scrapeYear(moviePageSoup)
        self.scrapeDirector(moviePageSoup)
        self.scrapeForeignTitle(blurayTitle)
        self.createBodyTitle()

    def formatSearchURL(self, title, year):
        startYear = int(year)-1
        endYear = int(year)+1
        self.searchURL = tplSearchURL % (helper.urlTransform("+",title),startYear,endYear)

    def scrapeIMDBLink(self, blurayRuntime):
        soup = BeautifulSoup(requests.get(self.searchURL).text, 'html.parser')
        searchResultList = soup.find_all("div", class_="lister-item mode-advanced")
        for result in searchResultList:
            runtimeList = result.find("span", class_="runtime")
            if runtimeList != None:
                runtime = int(result.find("span", class_="runtime").contents[0].strip().split(" ")[0].strip())
                if(abs(runtime-blurayRuntime) <= 3):
                    imdbCode = result.find("div", class_="ribbonize")
                    self.imdbCode = imdbCode.attrs['data-tconst']
                    self.movieURL = tplBaseURL % (self.imdbCode)

    def scrapePlotSummary(self):
        soup = BeautifulSoup(requests.get(self.movieURL+"/plotsummary").text, 'html.parser')
        plotSummarySoup = soup.find("ul", class_="ipl-zebra-list", id="plot-summaries-content")
        self.plotSummary = plotSummarySoup.contents[1].contents[1].get_text().strip()

    def scrapeYear(self, soup):
        self.year = soup.find("span", id="titleYear").get_text()[1:-1]
    
    def scrapeDirector(self, soup):
        directorSoup = soup.find("div", class_="credit_summary_item")
        self.director = directorSoup.get_text().split("\n")[2].strip()
    
    def scrapeForeignTitle(self, blurayTitle):
        releaseInfoSoup = BeautifulSoup(requests.get(self.movieURL+"/releaseinfo").text, 'html.parser')
        akaTableSoup = releaseInfoSoup.find("table", class_="ipl-zebra-list akas-table-test-only")
        akaResults = akaTableSoup.findAll("tr", class_="ipl-zebra-list__item aka-item")

        for result in akaResults:
            if result.contents[1].text.strip().lower() == "(original title)":
                self.foreignTitle = result.contents[3].text.strip()
            elif result.contents[1].text.strip().lower() == "usa":
                self.usaTitle = result.contents[3].text.strip()
            elif result.contents[1].text.strip().lower() == "world-wide (english title)":
                self.worldTitle = result.contents[3].text.strip()

    def createBodyTitle(self):
        englishTitle = ""

        if self.worldTitle != "":
            englishTitle = self.worldTitle
        else:
            englishTitle = self.usaTitle


        if self.foreignTitle == "" or self.foreignTitle == self.usaTitle or self.foreignTitle == self.worldTitle:
            self.bodyTitle = tplNonForeignBodyTitle % (englishTitle)
            return
        else:
            self.bodyTitle = tplForeignBodyTitle % (self.foreignTitle, englishTitle)
        
            
    def printAttrs(self):
        print(f"IMDB-URL: {self.movieURL}")
        print(f"IMDB-PLOT-SUMMARY: {self.plotSummary}")
        print(f"IMDB-YEAR: {self.year}")
        print(f"IMDB-DIRECTOR: {self.director}")
        print(f"IMDB-SEARCH-URL: {self.searchURL}")
        print(f"IMDB-FOREIGN-TITLE: {self.foreignTitle}")
        print(f"IMDB-USA-TITLE: {self.usaTitle}")
        print(f"IMDB-WORLD-TITLE: {self.worldTitle}")
        print(f"BODY-TITLE: {self.bodyTitle}")


        print()