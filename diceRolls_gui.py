import random
from tkinter import *
import dice as d

# Used in calculating the averageRoll roll of a dice 
# using brute force.
#NUMBER_TIMES = 1000000
#NUMLIST = []

# outputs the text to the windows GUI
def output(sumOfText, averageRoll, sumOfRoll, rollsOutput):
    sumLabel.config(text="Sum of " + sumOfText + " dice roll(s): " + str(sumOfRoll))
    averageRollLabel.config(text="averageRoll of " + sumOfText + " dice roll(s): " + str(averageRoll))
    rollLabel.config(text=rollsOutput)

# When the "advantage" button is pressed in the
# tkinter gui this function is called.
# textSend(advantage = true, disadvantage = false)
def advantage():
    textSend(True, False)

# When the "disadvantage" button is pressed in the
# tkinter gui this function is called.
# textSend(advantage = false, disadvantage = true)
def disadvantage():
    textSend(False, True)

# When the "Compute Dice" button is pressed in the
# tkinter gui this function is called.
# textSend(advantage = false, disadvantage = false)
# there is no way to send a textSend(advantage = true, disadvantage = true)
# so that case is unnecessary to deal with as of yet.
def normal():
    textSend(False, False)

# Main loop of program...
# Needs refactoring
# Reduce function length, seperate code into different function, etc...
def textSend(advantage, disadvantage):
    # diceTable holds each of the dice objects as they are created
    diceTable = []
    prompt = entry.get()
    textSum = ""
    # rollsOutput made by the user are outputted in
    # String format and stored in this variable
    rollsOutput = ""

    rollSum = 0
    averageRoll = 0
    largestRoll = 0
    smallestRoll = 0
    

    if len( prompt ) == 0:
        return

    while True:
        try:
            # while the inputted user text (dice rolls) exist
            # keep looping and adding the dice into the diceTable
            while len( prompt ) > 0:
                # foundPlus and foundD
                # Ensures correct input from user
                # Errors if improper format
                foundPlus = prompt.find( '+' )
                foundD = prompt.find( 'd' ) or prompt.find( 'D' )

                # if there are one or more '+' characters
                # add dice to table and loop again
                if foundPlus >= 0:
                    diceNum = int( prompt[0:foundD] )
                    dice = d.Dice( int(prompt[foundD+1:foundPlus]) )
                    prompt = prompt[foundPlus+1::]
                    diceTable.append( [dice, diceNum] )
                    continue
                # if 'd' or 'D' does not exist
                # improper format, output error
                elif foundD == -1:
                    raise ValueError
                # if there is no '+' character
                # only one dice roll exists
                # create dice and append to table
                else:
                    diceNum = int( prompt[0:foundD] )
                    dice = d.Dice( ( int(prompt[foundD+1::]) ) )
                    diceTable.append( [dice, diceNum] )
                    prompt = ""
            break
        except ValueError:
            break

    # Each dice in the table is an object.
    # We use that object's functions to roll the dice
    # based on their sides and based on the number
    # of that die.
    for i in range(len(diceTable)):
        currentDice = diceTable[i][0]
        # stores the value of the number of a specific dice roll
        # e.g. 5d20 (stores the 5).
        # the dice object holds the values of each roll
        # this could be handled better as 1d20 + 1d20 rolls two
        # different die seperately, while 2d20 rolls the two and adds the result...
        diceRollNum = diceTable[i][1]
        currentDice.roll(diceRollNum)

        rollsOutput += str(currentDice.outputRolls()) + "\n"
        averageRoll += currentDice.averageRoll()
        rollSum += currentDice.getRollSum()

        # Text handling
        if len(diceTable) == 1 or i == len(diceTable) - 1:
            textSum += str(diceRollNum) + "d" + str(currentDice.getSides())
        else:
            textSum += str(diceRollNum) + "d" + str(currentDice.getSides()) + " + "

        # Maximum and minimum rolls calculation
        if currentDice.getRollSum() > largestRoll:
            largestRoll = currentDice.getRollSum()
        if smallestRoll == 0:
            smallestRoll = currentDice.getRollSum()
        else:
            if smallestRoll < currentDice.getRollSum():
                pass
            else:
                smallestRoll = currentDice.getRollSum()

    # from GUI input, advantage or disadvantage
    if advantage and not disadvantage:
        rollsOutput += "Advantage Roll = " + str(largestRoll) + "\n"
    elif disadvantage and not advantage:
        rollsOutput += "Disadvantage Roll = " + str(smallestRoll) + "\n"

    # as soon as the input prompt has been properly reduced
    # to length 0, output the text.
    if len(prompt) == 0:
        output(textSum, averageRoll, rollSum, rollsOutput)
    else:
        rollLabel.config(text="Error. Please enter a valid input.")



window = Tk()
window.geometry("370x300")
window.resizable(False, False) 

window.winfo_toplevel().title("Dice Roll Calculator")
frame = Frame(window, relief=RAISED, borderwidth=1)
label = Label(text="Input as numDice[d]sideDice \n Example: 1d20 + 1d20 ")
entry = Entry(width=50)
button = Button(window, text="Compute Dice", width = 15, height = 1, command = normal)
button2 = Button(window, text="Advantage", width = 15, height = 1, command = advantage)
button3 = Button(window, text="Disadvantage", width = 15, height = 1, command = disadvantage)
rollLabel = Label(frame, text="")
sumLabel = Label(frame, text="")
averageRollLabel = Label(frame, text="")

entry.pack(side=TOP)
label.pack(side=TOP)
rollLabel.pack(side=TOP)
sumLabel.pack(side=TOP)
averageRollLabel.pack(side=TOP)
frame.pack(fill=BOTH, expand=True)
button2.pack(side=RIGHT, padx=5, pady=5)
button.pack(side=RIGHT, padx=5, pady=5)
button3.pack(side=RIGHT, padx=5, pady=5)

window.mainloop()


## Old code that calculated the averageRoll of a dice roll using brute force
## Only supports one dice at a time
# while True:
#     try:
#         prompt = input("What type of dice to roll (ex. 1d6, 2d8, etc): ")
#         diceNum = int(prompt[0:prompt.find('d')])
#         dice = int(prompt[prompt.find('d')+1::])
#         break
#     except ValueError:
#         print("Oops! Please enter dice format as [numberOfDice]d[highestDiceNum]")

# averageRoll = diceaverageRoll(diceNum, dice)

# numList.sort()

# # for i in range(len(numList)):
# #     count += 1
# #     if (not (i >= len(numList) - 1) and not (numList[i] == numList[i+1])) or (i >= NUMBER_TIMES * diceNum - 1):
# #         print(numList[i], "appears", (count), "times.")
# #         count = 0


# print("Sum of " + prompt + " dice rollsOutput: ", averageRoll) 