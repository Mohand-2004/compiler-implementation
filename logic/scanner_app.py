import re

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

tokenRegx = re.compile(
    '|'.join(
        f'(?P<{name}>{pattern})'
        for name, pattern in TOKEN_SPECIFICATION
    )
)

tokens = []

code = '''int main(void){
    // init variables
    int a,b;

    // get values 
    cin>>a>>b;

    // add values
    int sum = add(a,b);

    //print result
    cout<<"sum = "<<sum;
}'''

lines = code.split('\n')

for line in lines:
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

    data = newLine.strip()
    if not data.startswith("//"):

        for match in tokenRegx.finditer(data):
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'WHITESPACE':
                continue
            elif kind == 'CHAR':
                kind = 'SPECIAL_CHARACTER'
            # add token to token list
            tokens.append((kind, value))

for token in tokens:
    print(token)