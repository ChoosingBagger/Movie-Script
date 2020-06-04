import os
from pathlib import Path


class Folder(object):

    def __init___(self):
        self.movieDir = ""
        self.screenDir = ""

    def build(self, dir, title):
        self.createMovieDir(dir, title)
        self.createScreenDir()

    def createMovieDir(self, dir, title):
        dir = Path(dir)
        self.movieDir = dir / title
        if not os.path.exists(self.movieDir):
            os.makedirs(self.movieDir)

    def createScreenDir(self):
        self.screenDir = self.movieDir / "screens"
        if not os.path.exists(self.screenDir):
            os.makedirs(self.screenDir)
