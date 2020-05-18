# This file requires you set the path to BDInfoCLI-ng.exe in config.txt
# You can find this here: https://github.com/zoffline/BDInfoCLI-ng
from subprocess import run
from os import listdir
import configparser
from pathlib import Path


class BDInfo(object):

    def build(self, path, dir):
        path = Path(path)
        self.setPath(dir)
        self.runBDInfo(path)
        self.readBDInfo(dir)
        self.getWantedOutput()

    def setPath(self, dir):
        config = configparser.ConfigParser()
        config.read("conf.txt")
        bdinfoPath = config["user_settings"]["bdinfo"]
        self.outputDir = dir / "."
        self.bdinfo = Path(bdinfoPath)

    def runBDInfo(self, path):
        p = run([self.bdinfo, path, self.outputDir])

    def readBDInfo(self, dir):
        for file in listdir(dir):
            if file.startswith("BDINFO"):
                self.bdinfoText = dir / file

    def getWantedOutput(self):
        with open(self.bdinfoText, "r") as f:
            text = f.read()
            result = text.split("DISC INFO:", 1)
            result = result[1].split("FILES:", 1)
            self.prettyBDInfo = f"DISC INFO:{result[0]}".rstrip("\n")


# Debugging
if __name__ == "__main__":
    import bluray
    url = "https://www.blu-ray.com/movies/The-Lodge-Blu-ray/262879/"
    bdPath = r"F:\The Lodge 2019 1080p BluRay AVC DTS-HD MA 5.1-MTeam"
    blurayObj = bluray.Bluray(url)
    blurayObj.build()
    bdi = BDInfo()
    bdi.build(bdPath, directory.outputDir)
