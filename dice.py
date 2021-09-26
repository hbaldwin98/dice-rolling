import random

class Dice:

    def __init__(self, side):
        self.side = side
        self.rolls = []

    def roll(self, number):
        if number == 0:
            return 

        for i in range(number):
            self.rolls.append(random.randint(1, self.side))

        return self.rolls

    def outputRolls(self):
        text = "You rolled: "
        diceSum = 0
        rolls = self.rolls

        for i in range(len(rolls)):
            if i == 0:
                text += str(rolls[i])
                diceSum += rolls[i]
            else:
                diceSum += rolls[i]
                text += " + " + str(rolls[i])
        
        return text + " = " + str(diceSum)

    def averageRoll(self):
        return ((self.side + 1) / 2) * len(self.rolls)
    
    def getRolls(self):
        return self.rolls
    
    def getSides(self):
        return self.side
    
    def getRollSum(self):
        return sum(self.rolls)