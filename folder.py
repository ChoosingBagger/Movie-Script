import os
from pathlib import Path


class Folder(object):

    def __init___(self):
        self.outputDir = ""

    def build(self, dir, title):
        self.createMovieDir(dir, title)

    def createMovieDir(self, dir, title):
        dir = Path(dir)
        self.outputDir = dir / title
        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)
        return self.outputDir
