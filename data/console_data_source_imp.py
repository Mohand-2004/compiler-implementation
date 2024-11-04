from data.data_source import DataSource


class ConsoleDataSource(DataSource):
    
    def read(self):
        return input("Enter C source code: ")

    def write(self, data):
        print(data)