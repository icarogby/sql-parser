from sqlAlphabet import getAlphabet

class Parser():
    tokens = []
    alphabet = getAlphabet()

    def __init__(self, word) -> None:
        self.tokens = self.lexer(word)
    
    def lexer(self, word):
        for i in word.split(' '):
            if i in self.alphabet:
                self.tokens.append(i)
            else:
                raise Exception("Symbol not in alphabet")
        
        return self.tokens
    
    def nextToken(self):
        return True

x = Parser("hello")
