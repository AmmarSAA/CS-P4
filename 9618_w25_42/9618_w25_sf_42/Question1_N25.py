# a.i.
# Write program code to declare the class Bird and its constructor.
# Do not declare the other methods.
# All attributes should be private.
# Use your programming language appropriate constructor.
# If you are writing in Python, include attribute declarations using comments.

class Bird:
    def __init__(self, Species, DpH):
        self.__XPosition = 500.0 # Real
        self.__YPosition = 500.0 # Real
        self.__Species = Species # String
        self.__DistancePerHour = DpH # Real

# a.ii.
# The method GetSpecies() returns the species of the bird.
# Write program code for GetSpecies()

    def GetSpecies(self):
        return self.__Species

# a.iii.
# The method GetPosition() returns a string of the bird’s data in the format:
# "X = " & <XPosition> & " Y = " & <YPosition>
# An example string for a bird is:
# X = 500.0 Y = 250.0
# Write program code for GetPosition()

    def GetPosition(self):
        position = "X = " & str(self.__XPosition) & " Y = " & str(self.__YPosition)
        # position = f"X = {self.__XPosition} Y = {self.__YPosition}"
        return position

# a.iv.
# travelling north, vertical position increases
# travelling south, vertical position decreases.
# travelling east, horizontal position increases
# travelling west, horizontal position decreases.
# The method Move():
# • takes the direction of travel as a parameter in the form ‘N’ for north, ‘S’ for south,
# ‘E’ for east or ‘W’ for west
# • takes the number of minutes that the bird has been flying (to the nearest minute) as
# a parameter
# • calculates the distance travelled by the bird using the formula:
# distance travelled = (distance per hour / 60) * minutes flying
# • updates the vertical or horizontal position using the distance calculated.
# You do not need to validate the parameters.
# Write program code for Move()

    def Move(self, Direction, time):
        travelled = (self.__DistancePerHour / 60) * time
        if Direction = "N":
            self.__YPosition += travelled
        elif Direction = "S":
            self.__YPosition -= travelled
        elif Direction "E":
            self.__XPosition += travelled
        elif Direction "W":
            self.__XPosition -= travelled


# b.
# The main program creates two instances of Bird
# The first bird is the species ‘Cockatiel’ and flies 71.0 km/h.
# The second bird is the species ‘Macaw’ and flies 56.0 km/h.
# Write program code to declare and initialise the two birds.

def main():

    firstBird = Bird("Cockatiel", 71.0)
    secondBird = Bird("Macaw", 56.0)

    print(f"Species: {firstBird.GetSpecies()}, Position: {firstBird.GetPosition()}")
    print(f"Species: {secondBird.GetSpecies()}, Position: {secondBird.GetPosition()}")

    # bird = input("Enter the bird name to move [C/M]: ").lower()
    # direction = input("Enter the direction [N/S/E/W]: ").lower()
    # time = float(input("Enter the time to nearest minute: "))

    flag = False

    while not flag:
        if bird[0] == c or bird[0] == m:
            flag = True
        else:
            flag = False
            bird = input("Enter the bird name to move [C/M]: ").lower()
            bird = bird[0]
        
        if direction[0] == n or direction[0] == s or direction[0] == e or direction[0] == w:
            flag = True
        else:
            flag = False
            direction = input("Enter the direction [N/S/E/W]: ").lower()

        try:
            time = float(input("Enter the time to nearest minute: "))
            flag = True
        except:
            flag = False
            time = float(input("Re-Enter the CORRECT time to nearest minute: "))

    if flag:
        if bird[0] == c:
            firstBird.Move(direction, time)
            print(f"Species: {firstBird.GetSpecies()}, Position: {firstBird.GetPosition()}")
        else:
            secondBird.Move(direction, time)
            print(f"Species: {secondBird.GetSpecies()}, Position: {secondBird.GetPosition()}")




main()

# c.i.
# The main program needs to:
# Output a message that includes the species and current X position and Y position for each bird
# Prompt the user to select one of the birds to move and take this as an input
# Prompt the user to enter the direction the bird has been travelling and take this as an input
# Prompt the user to enter the time to the nearest minute that the bird has been travelling and take this as an input
# call the appropriate method to update the chosen bird’s position
# • output an update on the bird’s new position.
# Each input needs to repeat until valid data is entered. All outputs must be meaningful.
# Write program code to amend the main program