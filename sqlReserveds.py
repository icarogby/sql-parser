def getReserveds():
    reserveds = []
    
    with open("sqlReserveds.txt", "r") as file:
        for line in file:
            reserveds.append(line.strip())

    return reserveds