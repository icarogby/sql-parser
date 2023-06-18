from sqlParser import sqlParser

def main():
    with open ("comandos.txt", "r") as file:
        comandos = file.read()

    teste = sqlParser(comandos)
    # teste.printTokens()

if __name__ == "__main__":
    main()
