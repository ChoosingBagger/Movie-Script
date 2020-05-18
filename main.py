from bluray import Bluray
from imdb import IMDB
from rt import Tomato
from tmdb import MovieDB
from bdinfo import BDInfo
from folder import Folder
from configparser import ConfigParser
from args import getArgs
from omdb_api import OMDb
import helper


# blurayURL = ["https://www.blu-ray.com/movies/Bloodshot-Blu-ray/265952/", "https://www.blu-ray.com/movies/Vampire-Girl-vs-Frankenstein-Girl-Blu-ray/13951/", "https://www.blu-ray.com/movies/A-Star-Is-Born-Blu-ray/217109/", "https://www.blu-ray.com/movies/Better-Days-Blu-ray/261826/", "https://www.blu-ray.com/movies/Destry-Rides-Again-Blu-ray/131724/", "https://www.blu-ray.com/movies/Thieves-Blu-ray/263452/" ]
blurayURL = ["https://www.blu-ray.com/movies/The-Lodge-Blu-ray/262879/"]
# blurayURL = ["https://www.blu-ray.com/movies/A-Star-Is-Born-Blu-ray/217109/"]
config = ConfigParser()
config.read("conf.txt")
bdinfoPath = config["user_settings"]["bdinfo"]
tempDir = config["user_settings"]["output_dir"]

try:
    omdbKey = config["user_settings"]["omdb"]
    omKey = True
except KeyError:
    omKey = False
    pass

argsDict = getArgs()

for url in blurayURL:
    blurayObj = Bluray(url)
    blurayObj.build()
    # blurayObj.printAttrs()

    directory = Folder()
    directory.build(tempDir, blurayObj.title)

    if omKey:
        omdbObj = OMDb()
        omdbObj.build(blurayObj.title, blurayObj.year, omdbKey)
    else:
        imdbObj = IMDB()
        imdbObj.build(blurayObj.title, blurayObj.year, blurayObj.runtime)
        # imdbObj.printAttrs()

    # tmdbObj = MovieDB()
    # titleDict = [imdbObj.worldTitle, imdbObj.foreignTitle, imdbObj.usaTitle, blurayObj.title]
    # tmdbObj.build(titleDict, blurayObj.year)

    # rtObj = Tomato()
    # rtObj.build(blurayObj.title, tmdbObj.year)
    # rtObj.printAttrs()

    if argsDict.bdinfo:
        bdiObj = BDInfo()
        bdiObj.build(argsDict.bdinfo, directory.outputDir)
        print(bdiObj.prettyBDInfo)
