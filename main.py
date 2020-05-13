import bluray
import helper
import imdb


blurayURL = ["https://www.blu-ray.com/movies/Bloodshot-Blu-ray/265952/", "https://www.blu-ray.com/movies/Vampire-Girl-vs-Frankenstein-Girl-Blu-ray/13951/", "https://www.blu-ray.com/movies/A-Star-Is-Born-Blu-ray/217109/", "https://www.blu-ray.com/movies/Better-Days-Blu-ray/261826/", "https://www.blu-ray.com/movies/Destry-Rides-Again-Blu-ray/131724/", "https://www.blu-ray.com/movies/Thieves-Blu-ray/263452/" ]

for url in blurayURL:
    blurayObj = bluray.Bluray(url)
    blurayObj.build()
    #blurayObj.printAttrs()
    
    imdbObj = imdb.IMDB()
    imdbObj.build(blurayObj.title, blurayObj.year, blurayObj.runtime)
    imdbObj.printAttrs()


