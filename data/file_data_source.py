from data.data_source import DataSource
from logic.models.grammer import Grammer


class FileDataSource(DataSource):
    def __init__(self,inPath,outPath = None):
        self.inPath = inPath
        self.outPath = self.inPath if outPath is None else outPath
        super().__init__()
    def read(self):
        with open(self.inPath, "r") as f:
            return f.read()
        
    def readGrammer(self):
        with open(self.inPath, "r") as f:
            return Grammer.fromString(f.read())

    def write(self, data):
        with open(self.outPath, "w") as f:
            f.write(data)