from sqlAlphabet import getAlphabet
from sqlReserveds import getReserveds

class Parser():
    tokens = []
    i = -1
    alphabet = getAlphabet()
    reserveds = getReserveds()

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

                elif i == (len(word) - 1):
                    self.tokens.append(word[begin:])
                    
                    reading = False

            else:
                if word[i] == " ":
                    pass
                elif word[i] in "=*()[],;":
                    self.tokens.append(word[i])
                else:
                    reading = True
                    begin = i

        self.makeToken(self.tokens)

    def makeToken(self, tokens):
        for i in range(len(tokens)):
            if tokens[i] not in self.reserveds:
                if tokens[i].isdigit():
                    tokens[i] = ("value", int(tokens[i]))
                else:
                    tokens[i] = (("id", tokens[i]))

    def getToken(self):
        self.i += 1

        if self.i < len(self.tokens):
            return self.tokens[self.i]
        else:
            raise Exception("No more tokens")
    
    def printTokens(self):
        print(self.tokens)
    
top = Parser("SELECT 98 FROM idaqui 46;")
top.printTokens()
