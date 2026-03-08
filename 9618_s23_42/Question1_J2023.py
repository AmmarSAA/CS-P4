# a
Animals = [] * 10  # Array of 10 elements of type string


# c
def SortDescending():
    global Animals
    ArrayLength = len(Animals)
    Temp = ""
    for x in range(0, ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = Temp


def main():

    # b
    Animals.append("horse".lower())
    Animals.append("lion".lower())
    Animals.append("rabbit".lower())
    Animals.append("mouse".lower())
    Animals.append("bird".lower())
    Animals.append("deer".lower())
    Animals.append("whale".lower())
    Animals.append("elephant".lower())
    Animals.append("kangaroo".lower())
    Animals.append("tiger".lower())

    # d)i
    SortDescending()
    for i in range(0, len(Animals)):
        print(Animals[i])


main()
