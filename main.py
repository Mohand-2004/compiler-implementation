from data.file_data_source import FileDataSource
from logic.scanner import Scanner

tokens = Scanner(
    dataSource = FileDataSource(
        intputPath = r"test.txt",
    )
).tokens


FileDataSource(intputPath=r"output.txt").write("\n".join([str(i) for i in tokens]))
