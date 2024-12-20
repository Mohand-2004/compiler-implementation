from logic.models.rule import Rule


class Grammer:
    def __init__(self,rules: list) -> None:
        # init rules
        self.rules = rules

        # init nonterminals and terminals
        self.nonterminals = set()
        self.terminals = set()
        for rule in self.rules:
            ruleStr = rule.left + rule.right
            for char in ruleStr:
                if char.isupper():
                    self.nonterminals.add(char)
                else:
                    self.terminals.add(char)

        # convert sets to lists
        self.nonterminals = list(self.nonterminals)
        self.terminals = list(self.terminals)


    @classmethod
    def fromConsole(cls):
        rules = []
        for i in range(int(input("number of rules: "))):
            rules.append(Rule.fromString(input(f"rule {i+1}: ")))
        return Grammer(rules)
    
    @classmethod
    def fromString(cls,string):
        return Grammer([Rule.fromString(rule) for rule in string.split('\n')])
    

    def isSimple(self) -> bool:
        # check for left side
        for rule in self.rules:
            if len(rule.left) > 1 or rule.right[0].isupper():
                return False

        # check for disjoint
        startingSymbols = {nonterminal:[] for nonterminal in self.nonterminals}
        for rule in self.rules:
            if rule.right[0] in startingSymbols[rule.left]:
                return False
            startingSymbols[rule.left].append(rule.right[0])

        return True


    def __str__(self) -> str:
        return '\n'.join([str(rule) for rule in self.rules])

        
