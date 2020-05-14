from requests import get


class Tomato(object):
    def __init__(self):
        self.api_url = "https://www.rottentomatoes.com/api/private/v2.0/search"
        self.rtSearh = ""
        self.prefix = ""
        self.count = ""

    def build(self, term):
        r = get(url=self.api_url, params={"q": term})
        self.rtSearch = r.json()
        self.scrapeCount()
        self.scrapeURL()

    def scrapeCount(self):
        # if flag_in_future == "movie":
        #     self.prefix = "movie"
        # else:
        #     self.prefix = "tv"
        # Remove below before production
        self.prefix = "movie"
        self.count = str(self.rtSearh[f"{self.prefix}Count"])

    def scrapeURL(self):
        self.url = "https://www.rottentomatoes.com/"
        dicts = {}
        listTitle = []
        listURL = []
        if self.prefix == "movie":
            self.prefix = "movies"
        else:
            self.prefix = "tvSeries"
        for items in self.rtSearh[self.prefix]:
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
