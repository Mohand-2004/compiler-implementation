from data.console_data_source_imp import ConsoleDataSource
from data.file_data_source import FileDataSource
from logic.parser import Parser
from logic.scanner import Scanner

parser = Parser(
    dataSource = FileDataSource(
        inPath = 'grammer.txt',
        outPath = 'grammer_output.txt',
    )
)

if parser.parse(input('Enter Your String: ')):
    print('Your String Is Accepted !')
else:
    print('Your String Is Rejected !')


print('Stack after parsing :',end=' ')
parser.stack.print()
# print('=============================================')
# print('1-Another Grammer\n2-Another String\n3-Exit')  
# usreChoice = int(input('Enter Your Choice: ')) 
# while usreChoice != 3:
#     if usreChoice == 1:
#         parser.reDifineGrammer()
#         if parser.parse(input('Enter Your String: ')):
#             print('Your String Is Accepted !')
#         else:
#             print('Your String Is Rejected !')
#     elif usreChoice == 2:
#         if parser.parse(input('Enter Your String: ')):
#             print('Your String Is Accepted !')
#         else:
#             print('Your String Is Rejected !')
#     print('Stack after parsing :',end=' ')
#     parser.stack.print()
#     print('=============================================')
#     print('1-Another Grammer\n2-Another String\n3-Exit')
#     usreChoice = int(input('Enter Your Choice: '))


# scanner = Scanner(
#     dataSource=FileDataSource(
#         intputPath='test.txt',
#         outputPath='output.txt'
#     )
# )

