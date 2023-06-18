from sqlAlphabet import getAlphabet
from sqlReserveds import getReserveds
from sqlTipos import getTipos

class sqlParser():
    tokens = []
    i = -1
    alphabet = getAlphabet()
    reserveds = getReserveds()
    tipos = getTipos()
    token = ""

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

        self.tokens.append("$")
        self.printTokens()
        self.parser(self.tokens)


    def getToken(self) -> str:
        self.i += 1

        if self.i < len(self.tokens):
            return self.tokens[self.i]
        else:
            raise Exception("No more tokens")
        
    def parser(self, tokens):
        self.init()
        print("reconhecido")
    
    # DISGRAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    def init(self):
        self.token = self.getToken()

        if self.token == "USE":
            self.ID()

            token = self.getToken()
            
            if token != ";":
                raise Exception("; expected")
            
            self.init()
        
        elif self.token == "CREATE":
            self.create()
            self.init()

        elif self.token == "$":
            pass

        else:
            raise Exception("USE or CREATE expected")
    
    def create(self):
        self.token = self.getToken()

        if self.token == "TABLE":
            self.ID()

            self.token = self.getToken()

            if self.token != "(":
                raise Exception("( expected")
            
            self.createTable()

            self.token = self.getToken()

            if self.token != ";":
                raise Exception("; expected")

        elif self.token == "DATABASE":
            self.ID()
            
            self.token = self.getToken()

            if self.token != ";":
                raise Exception("; expected")
        else:
            raise Exception("TABLE or DATABASE expected")
    
    def createTable(self):
        self.ID()
        self.TIPO()

        self.token = self.getToken()

        if self.token == ",":
            self.createTable()

        elif self.token != ")":
            raise Exception(") expected")

    def ID(self):
        self.token = self.getToken()

        if self.token[0].isdigit() or self.token.isdigit() or (self.token in self.reserveds):
            raise Exception("id expected")
        
    def TIPO(self):
        self.token = self.getToken()

        if self.token not in self.tipos:
            raise Exception("INT or VARCHAR expected")

    def printTokens(self):
        print(self.tokens)
    
top = sqlParser("CREATE TABLE id (top INT, ferias VARCHAR); CREATE DATABASE id; USE rayray;")
