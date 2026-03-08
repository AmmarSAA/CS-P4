# a.
class TreasureChest:
    def __init__(self, q, ans, points):
        self.__question = q  # String
        self.__answer = ans  # Integer
        self.__points = points  # Integer

    # c.i.
    def getQuestion(self):
        return self.__question

    # c.ii
    def checkAnswer(self, ans):
        return self.__answer == ans

    # c.iii
    def getPoints(self, numAttempt):
        match numAttempt:
            case 1:
                return self.__points
            case 2:
                return self.__points // 2
            case 3:
                return self.__points // 4
            case 4:
                return self.__points // 4
            case _:
                return 0


# b.
# TreasureChest("0", 0, 0)
arrayTreasure = [] * 4


def readData():
    global arrayTreasure
    questions = []
    answers = []
    points = []
    try:
        file = open(
            "F:\\Data\\P4\\9618_s21_41\\9618_s21_sf_41\\06_9618_41_Confidential Source Files June 2021\\06_9618_41_Confidential Source Files June 2021\\TreasureChestData.txt",
            "r",
        )
    except Exception as e:
        print("Error: ", e)
    else:
        wholeFile = file.read().splitlines()
        for i in range(0, len(wholeFile), 3):
            questions.append(wholeFile[i])
            # print(questions)
        for i in range(1, len(wholeFile), 3):
            answers.append(int(wholeFile[i]))
            # print(answers)
        for i in range(2, len(wholeFile), 3):
            points.append(int(wholeFile[i]))
            # print(points)

    for i in range(len(questions)):
        arrayTreasure.append(TreasureChest(questions[i], answers[i], points[i]))
        # print(arrayTreasure.__question)


# c.iv.
def main():
    readData()
    numAttempt = 1
    # question = readData()
    qNum = int(input("Enter the question number between 1 and 5: "))
    while qNum > 6 or qNum < 0:
        qNum = int(input("Please Enter the question number between 1 and 5: "))
    question = int(input(f"What is {arrayTreasure[qNum-1].getQuestion()}: "))
    answer = arrayTreasure[qNum - 1].checkAnswer(question)
    while not answer:
        answer = arrayTreasure[qNum - 1].checkAnswer(
            int(input("WRONG ANSWER! Re-Enter the answer of the question: "))
        )
        numAttempt += 1

    print(f"Your Points: {arrayTreasure[qNum - 1].getPoints(numAttempt)}")


main()
