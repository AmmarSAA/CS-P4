class TreasureChest:
    def __init__(self, q, ans, points):
        self.__q = q
        self.__ans = ans
        self.__points = points

    # i
    def getQuestion(self):
        return self.__q

    # iii
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points / 2
        elif attempts == 3 or attempts == 4:
            return self.__points / 4
        else:
            return 0

    # ii
    def checkAnswer(self, uAns):
        if uAns == self.__ans:
            return True
        else:
            return False


arrayTreasure = [TreasureChest(0, 0, 0) for _ in range(1, 6)]


# b
def readData():
    global arrayTreasure

    try:
        with open(
            "F:\\CS-P4\\9618_s21_42\\9618_s21_sf_42\\06_9618_42_Confidential Source Files June 2021\\06_9618_42_Confidential Source Files June 2021\\TreasureChestData.txt"
        ) as f:
            file = f.readlines()
            y = 0
            for i in range(5):
                arrayTreasure[i] = TreasureChest(
                    file[y].strip(), int(file[y + 1].strip()), int(file[y + 2].strip())
                )
                y += 3

    except Exception as e:
        print(f"The error: {e}")


# main
readData()
question = int(input("Enter the question number between 1 and 5: ")) - 1
attempts = 1
answer = int(input(f"Enter the answer of {arrayTreasure[question].getQuestion()}: "))
check = arrayTreasure[question].checkAnswer(answer)
while check == False:
    attempts += 1
    answer = int(
        input(f"Enter the answer of {arrayTreasure[question].getQuestion()}: ")
    )
    check = arrayTreasure[question].checkAnswer(answer)

print(f"Your points are: {arrayTreasure[question].getPoints(attempts)}")
