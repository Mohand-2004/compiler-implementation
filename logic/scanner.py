from logic.models.token_model import Token
import re

class Scanner:
    # cpp language regexs
    TOKEN_SPECIFICATION = [
        ('COMMENT', r'//.*'),
        ('KEYWORD', r'\b(?:int|float|char|if|else|for|while|return|void|switch|case|break|continue|default|do|typedef|struct|union|enum|const|sizeof|unsigned)\b'),
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('NUMBER', r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b'),
        ('OPERATOR', r'[+\-*/%=&|<>!]=?|&&|\|\|'),
        ('SPECIAL_CHARACTER', r'[{}()\[\],;<>]'),        
        ('STRING', r'"(\\.|[^"\\])*"'),
        ('CHAR', r"\'(\\.|[^'\\])\'"),
        ('PREPROCESSOR', r'#\s*(?:include|define)\b.*'),
        ('WHITESPACE', r'\s+'),
    ]

    # token regex
    tokenRegx = re.compile(
        '|'.join(
            f'(?P<{name}>{pattern})'
            for name, pattern in TOKEN_SPECIFICATION
        )
    )
    def __init__(self,dataSource):
        # data source
        self.dataSource = dataSource

        # init empty token list
        self.tokens = []

        # read source code
        data = self.dataSource.read()

        # splite the code to lines
        data = data.split("\n")

        # scan each line
        for line in data:
            self.scan(self.removeInlineComments(line))

    def scan(self,data):
        data = data.strip()
        if not data.startswith("//"):

            for match in self.tokenRegx.finditer(data):
                kind = match.lastgroup
                value = match.group(kind)
                if kind == 'WHITESPACE':
                    continue
                elif kind == 'CHAR':
                    kind = 'SPECIAL_CHARACTER'
                # add token to token list
                self.tokens.append(Token(kind, value))
    
    # removes inline comments
    def removeInlineComments(self,line):
        newLine = ''
        push = True
        for i in range(len(line)):
            if i+1 < len(line) and line[i] == '/' and line[i+1] == '*':
                push = False
            elif i-1 > 0 and line[i] == '/' and line[i-1] == '*':
                push = True
                continue
            elif i+1 < len(line) and line[i] == '/' and line[i+1] == '/':
                break
            if push:
                newLine += line[i]
        return newLine