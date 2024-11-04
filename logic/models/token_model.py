class Token:

    def __init__(self, tokenType, tokenValue):
        self.type = tokenType  
        self.value = tokenValue
        self.position = None

    def __str__(self):
        return f"< {self.type} : {self.value} >"