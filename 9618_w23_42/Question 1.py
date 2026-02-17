# a.i
StackVowel = [] * 100  # Global arrray of Strings
StackConsonant = [] * 100  # Global arrray of Strings

# a.ii
VowelTop = 0  # global variable of datatype integer
ConsonantTop = 0  # global variable of datatype integer

msg = ""


# b.i
def PushData(letter):

    global VowelTop, ConsonantTop, StackConsonant, StackVowel, msg
    if letter.lower() in ["a", "e", "i", "o", "u"]:

        if VowelTop < 100:
            StackVowel.append(letter)
            VowelTop += 1
        else:
            msg = f"Vowel Stack is full!"
    else:
        if ConsonantTop < 100:
            StackConsonant.append(letter)
            ConsonantTop += 1
        else:
            msg = f"Consonant Stack is full!"

    if msg:
        print(msg)


# b.ii
def ReadData():
    try:
        with open(
            "./9618_w23_42/9618_w23_sf_42/11_9618_42_SourceFiles/StackData.txt", "r"
        ) as f:
            alphabets = f.read().splitlines()
            for letter in alphabets:
                PushData(letter)

    except Exception as e:
        msg = f"Error: {e}"
        print(msg)


# c.
def PopVowel():
    global VowelTop, StackVowel
    VowelTop -= 1
    if VowelTop < 0:
        value = "No Data in Vowel Stack"
    else:
        value = StackVowel[VowelTop]

    return value


def PopConsonant():
    global ConsonantTop, StackConsonant
    ConsonantTop -= 1
    if ConsonantTop < 0:
        value = "No Data in Consonant Stack"
    else:
        value = StackConsonant[ConsonantTop]

    return value


# d.i.
def main():

    ReadData()
    global msg
    for i in range(1, 6):
        uChoice = input("Choose vowel or consonant: ")
        if uChoice.lower()[0] == "v":
            msg += PopVowel()
        else:
            msg += PopConsonant()

    print(msg)


main()

# ReadData()
# msg = ""
# print(msg)

# print(VowelTop)
# print(StackVowel)
# print(ConsonantTop)
# print(StackConsonant)
