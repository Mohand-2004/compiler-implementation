from data.data_source import DataSource
from logic.models.grammer import Grammer


class ConsoleDataSource(DataSource):
    
    def read(self,massage=""):
        return input(massage)
    
    def readGrammer(self):
        return Grammer.fromConsole()

    def write(self, data):
        print(data)