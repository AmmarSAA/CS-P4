class EventItem:
    def __init__(self, EventName, Type, Difficulty):
        self.__EventName = EventName  # String
        self.__Type = Type  # String
        self.__Difficulty = Difficulty  # Integer

    def GetName(self):
        return self.__EventName

    def GetType(self):
        return self.__Type

    def GetDifficulty(self):
        return self.__Difficulty


class Character:
    def __init__(self, CharacterName, Jump, Swim, Run, Drive):
        self.__CharacterName = CharacterName  # STRING
        self.__Jump = Jump  # INTEGER
        self.__Swim = Swim  # INTEGER
        self.__Run = Run  # INTEGER
        self.__Drive = Drive  # INTEGER

    def GetName(self):
        return self.__CharacterName
    def CalculateScore(self, Type,Difficulty):
        Score = 0

        if Type.lower() == "jump":
            SkillLvl = self.__Jump
        elif Type.lower() == "swim":
            SkillLvl = self.__Swim
        elif Type.lower() == "run":
            SkillLvl = self.__Run
        elif Type.lower() == "drive":
            SkillLvl = self.__Drive

        if SkillLvl >= Difficulty:
            Score = 100
        else:
            Difference = SkillLvl - Difficulty

            if Difference == 1:
                Score = 80
            elif Difference == 2:
                Score = 60
            elif Difference == 3:
                Score = 40
            elif Difference == 4:
                Score = 20

        return Score


def main():
    Group = [EventItem("", "", 0) for _ in range(5)]

    Group[1] = EventItem("Bridge", "jump", 3)
    Group[2] = EventItem("Water Wade", "swim", 4)
    Group[3] = EventItem("100 mile run", "run", 5)
    Group[4] = EventItem("Gridlock", "drive", 2)
    Group[5] = EventItem("Wall on wall", "jump", 4)


    Tarz = Character("Tarz", 5,3,5,1)
    Geni = Character("Geni", 2,2,3,4)
    TarzScores = []
    GeniScores = []
    TarzPoints = []
    GeniPoints = []

    for i in range(5):
        TarzScores.append(Tarz.CalculateScore(Group[i].GetType(), Group[i].GetDifficulty()))
        GeniScores.append(Geni.CalculateScore(Group[i].GetType(),Group[i].GetDifficulty()))

        for Score in TarzScores:
            if TarzScores[Score] > GeniScores[Score]:
                TarzPoints.append()



main()
