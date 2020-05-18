from requests import get


class Tomato(object):
    def __init__(self):
        self.api_url = "https://www.rottentomatoes.com/api/private/v2.0/search"
        self.url = "https://www.rottentomatoes.com/m/"
        self.rtSearch = ""
        self.prefix = ""
        self.count = ""

    def build(self, term, year):
        term_formatted = term.split()
        term_formatted = "_".join(term_formatted)
        self.movie_url = f"{self.url}{term_formatted}_{year}"
        # print(self.movie_url)
        r = get(url=self.api_url, params={"q": term_formatted})
        self.rtSearch = r.json()

    def scrapeCount(self):
        # if flag_in_future == "movie":
        #     self.prefix = "movie"
        # else:
        #     self.prefix = "tv"
        # Remove below before production
        self.prefix = "movie"
        self.count = self.rtSearch[f"{self.prefix}Count"]
        # print(self.count)

    def scrapeURL(self):

        dicts = {}
        listTitle = []
        listURL = []
        if self.prefix == "movie":
            self.prefix = "movies"
        else:
            self.prefix = "tvSeries"
        for items in self.rtSearch[self.prefix]:
            listTitle.append(items["name"])
            tempURL = items["url"]
            listURL.append(f"{self.url}{tempURL}")
        #print(listTitle)
        #print(listURL)

        for key in listTitle:
            for value in listURL:
                dicts[key] = value
                listURL.remove(value)
                break
        #print(dicts)

    def printAttrs(self):
        print()
        # print(f"RT-JSON: {self.rtSearh}")
        # print(f"RT-PREFIX-COUNT: {self.count}")
