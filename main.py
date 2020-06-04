from bluray import Bluray
from imdb import IMDB
from tmdb import MovieDB
from bdinfo import BDInfo
from folder import Folder
from configparser import ConfigParser
from args import getArgs
from template import Template
import helper


blurayURL = [
    "https://www.blu-ray.com/movies/Bloodshot-Blu-ray/265952/",
    "https://www.blu-ray.com/movies/Vampire-Girl-vs-Frankenstein-Girl-Blu-ray/13951/",
    "https://www.blu-ray.com/movies/A-Star-Is-Born-Blu-ray/217109/",
    "https://www.blu-ray.com/movies/Better-Days-Blu-ray/261826/",
    "https://www.blu-ray.com/movies/Destry-Rides-Again-Blu-ray/131724/",
    "https://www.blu-ray.com/movies/Thieves-Blu-ray/263452/"
    ]
config = ConfigParser()
config.read("conf.txt")
bdinfoPath = config["user_settings"]["bdinfo"]
tempDir = config["user_settings"]["output_dir"]
argsDict = getArgs()

for url in blurayURL:
    blurayObj = Bluray(url)
    blurayObj.build()
    blurayObj.printAttrs()

    directory = Folder()
    directory.build(tempDir, blurayObj.title)

    imdbObj = IMDB()
    imdbObj.build(blurayObj.imdbLink, blurayObj.title, blurayObj.year, blurayObj.runtime)
    imdbObj.printAttrs()

    tmdbObj = MovieDB()
    tmdbObj.build(blurayObj.imdbLink, directory.movieDir)
    tmdbObj.printAttrs()

    if argsDict.bdinfo:
        bdiObj = BDInfo()
        bdiObj.build(argsDict.bdinfo, directory.movieDir)
        print(bdiObj.prettyBDInfo)

    # templateObj = Template()
    # templateObj.build(
    #    imdbObj.worldTitle, imdbObj.director, aimgObj.poster, blurayObj.imdbLink,
    #    tmdbObj.url, blurayObj.rtLink, blurayURL, imdbObj.plotSummary,
    #    argsDict.file, blurayObj,movieDistributor, blurayObj.country,
    #    imdbObj.year, imgObj.bbcode, imdbObj.bodyTitle
    #    )
