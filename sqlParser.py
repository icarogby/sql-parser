from sqlAlphabet import getAlphabet

class Parser():
    tokens = None
    alphabet = getAlphabet()

    def __init__(self, word) -> None:
        self.tokens = self.lexer(word)
    
    def lexer(self, word):
        for i in word:
            if i not in self.alphabet:
                raise Exception("Symbol not in alphabet")
            
        for token in word.split(' '):
            yield token
    
    def getToken(self):
        return next(self.tokens)
    
top = Parser("select from table")
print(top.getToken())
print(top.getToken())
