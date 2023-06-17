from sqlAlphabet import getAlphabet

class Parser():
    tokens = []
    i = -1
    alphabet = getAlphabet()

    def __init__(self, word) -> None:
        self.lexer(word)
    
    def lexer(self, word):
        reading = False
        begin = 0

        for i in range(len(word)):
            if word[i] not in self.alphabet:
                raise Exception("Symbol not in alphabet")

            if reading:
                if word[i] in "=*()[],; ":
                    self.tokens.append(word[begin:i])

                    if word[i] != " ":
                        self.tokens.append(word[i])
                    
                    reading = False

            else:
                if word[i] == " ":
                    pass
                elif word[i] in "=*()[],;":
                    self.tokens.append(word[i])
                else:
                    reading = True
                    begin = i

    def getToken(self):
        self.i += 1

        if self.i < len(self.tokens):
            return self.tokens[self.i]
        else:
            raise Exception("No more tokens")
    
    def printTokens(self):
        print(self.tokens)
    
top = Parser("SELECT idaqui [, idaqui]* FROM idaqui;")
top.printTokens()
