def getAlphabet():
    alphabet = ""
    
    with open("sqlAlphabet.txt", "r") as file:
        alphabet = file.read()

    return alphabet
