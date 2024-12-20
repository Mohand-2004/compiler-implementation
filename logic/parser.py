from data.data_source import DataSource
from logic.models.grammer import Grammer
from logic.models.rule import Rule
from logic.models.stack import Stack


class Parser:
    def __init__(self,dataSource: DataSource) -> None:
        self.dataSource = dataSource
        self.grammer = dataSource.readGrammer()

        while not self.grammer.isSimple():
            print('Grammer is not simple')
            self.grammer = dataSource.readGrammer()

        self.rulesMap = {(rule.left + rule.right[0]): rule.right for rule in self.grammer.rules}
        self.stack = Stack()

    def reDifineGrammer(self,) -> None:
        self.grammer = self.dataSource.readGrammer()

        while not self.grammer.isSimple():
            self.grammer = self.dataSource.readGrammer()

        self.rulesMap = {(rule.left + rule.right[0]): rule.right for rule in self.grammer.rules}
        self.stack = Stack()


    def parse(self,string) -> bool:
        self.stack = Stack()
        # add start symbol to stack
        self.stack.push(self.grammer.rules[0].left)

        # init starting symbols
        startingSymbols = {nonterminal:[] for nonterminal in self.grammer.nonterminals}
        for rule in self.grammer.rules:
            startingSymbols[rule.left].append(rule.right[0])


        for char in string:
            if self.stack.peek().isupper():
                if char in startingSymbols[self.stack.peek()]:
                    value =  self.stack.pop()
                    for c in self.rulesMap[value + char][1:][::-1]:
                        self.stack.push(c)
                else:
                    return False
            else:
                if self.stack.peek() == char:
                    self.stack.pop()
                else:
                    return False

        return self.stack.lenght() == 0
