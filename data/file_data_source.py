from data.data_source import DataSource


class FileDataSource(DataSource):
    def __init__(self,intputPath,outputPath = None):
        self.inPath = intputPath
        self.outPath = self.inPath if outputPath is None else outputPath
        super().__init__()
    def read(self):
        with open(self.inPath, "r") as f:
            return f.read()

    def write(self, data):
        with open(self.outPath, "w") as f:
            f.write(data)