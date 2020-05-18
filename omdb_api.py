from omdb import OMDBClient
import json


class OMDb(object):

    def build(self, title, year, apikey):
        client = OMDBClient(apikey=apikey)
        self.search(client, title, year)
        self.parse(self.result)

    def search(self, client, title, year):
        search = client.request(t=title, y=year)
        self.result = json.loads(search.content)

    def parse(self, result):
        print(result["imdbID"])
