# Stronghold Locator
# Author: Austin Boydston
# Description: This program takes in the coordinates and angle of
# two different eye of ender throws and calculates the location of 
# the stronghold.


prompt1 = "What is the x coordinate of the first throw?"
prompt2 = "What is the y coordinate of the first throw?"
prompt3 = "What is the angle of the first throw?"
prompt4 = "What is the x coordinate of the second throw?"
prompt5 = "What is the y coordinate of the second throw?"
prompt6 = "What is the angle of the second throw?"


def getInputNumber(prompt):
    while True:
        print(prompt)
        UserInput = input()
        try:
            UserInputNumber = float(UserInput)
        except ValueError:
            print("Incorrect Input, enter a number only")
        else:
            return UserInputNumber

def triangulate(x1, y1, theta1, x2, y2, theta2):
    pass


x1 = getInputNumber(prompt1)
y1 = getInputNumber(prompt2)
theta1 = getInputNumber(prompt3)
x2 = getInputNumber(prompt4)
x2 = getInputNumber(prompt5)
theta2 = getInputNumber(prompt6)


