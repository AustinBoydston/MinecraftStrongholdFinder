# Stronghold Locator
# Author: Austin Boydston
# Description: This program takes in the coordinates and angle of
# two different eye of ender throws and calculates the location of 
# the stronghold.
import math as m

prompt1 = "What is the x coordinate of the first throw?"
prompt2 = "What is the z coordinate of the first throw?"
prompt3 = "What is the angle of the first throw?"
prompt4 = "What is the x coordinate of the second throw?"
prompt5 = "What is the z coordinate of the second throw?"
prompt6 = "What is the angle of the second throw?"



################ Unit Tests ################
#Test the slope function
def slopeUnitTest():
    x1 = 2
    y1 = 3
    x2 = 6
    y2 = 8
    m = slope(x1, y1, x2, y2)
    if m == 5/4:
        print("Slope Unit Test 1 Passed")
    else:
        print("Slope Unite Test 1 Failed")
        print(m)
        print(5/4)
    
    x1 = 3.201
    y1 = 7.239
    x2 = 5.489
    y2 = 9.237 
    m = slope(x1, z1, x2, z2)

    if round(m, 7) == round(1.998/2.288, 7):
        print("Slope Unit Test 2 Passed")
    else:
        print("Slope Unit Test 2 Failed")
        print(m)
        print(1.998/2.288)



#Test the distance function
def distanceUnitTest():
    dist1 = distance(1, 2, 3, 4)
    if int(dist1) == int(2.8284271247462):
        print("Diatance Unit Test 1 Passed")
    else:
        print("Distance Unit Test 1 Failed")
    
    dist1 = distance(4.55553, 13.2223, 0.111, -1000.34)
    if int(dist1) == int(1013.5720447152):
        print("Distance Unit Test 2 Passed")
    else: 
        print("Diatance Unit Test 2 Failed")

#Unit Test for the function that gets another point along the line
def getSecondPointUnitTest():
    x1 = 2
    y1 = 2
    theta = 90
    val = getSecondPoint(x1, y1, theta)
    if val[0] == 2 and val[1] == 3:
        print("Get Second Point Unit Test Passed")
    else:
        print("Get Second Point Unit Test Failed")
        print(val[0], ", ", val[1])
    
    #test 2
    #x1 = 
    

    
#Get a number from the user. The prompt gives the user the numbers meaning
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

#Calculate the distance between two points
def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

#convert the angle measure from degrees to radians
def degreeToRad(theta):
    return theta * (m.pi / 180)

#Get a point along the give line/vector
def getSecondPoint(x1, y1, theta):
    x3 =  m.cos(degreeToRad(theta)) + x1    
    y3 =  m.sin(degreeToRad(theta)) + y1
    return x3, y3

#gets the slope of the given arguments
def slope(x1, y1, x2, y2):
    return (y1 - y2)/(x1 - x2)


# find the y-intercept for the given line
def findB(m, x1, y1):
    return y1 - m*x1

#Get the x coordinate of the stronghold
def findStrongholdX(m1, m2, b1, b2):
    x = (b2 - b1)/(m1 - m2)
    return x

#Get the Y coordinate of the strong hold
def findStrongholdY(x, m, b):
    return (m*x + b)

#Get the cartesian angle from the minecraft angle
def convertToStandardAngle(theta):
    theta = theta % 180
    if theta < 0:
        theta = -theta
    else:
        theta = 1 - theta + 180
    #theta = theta + 180
    return theta

#convert the coordinates to standard cartesian coordinates.
def convertCoordsToStandard(x,z):
    return z, x

def convertCoordsToMC(x, y):
    return x, -y

def triangulate(x1, y1, theta1, x2, y2, theta2):
    #Get an additional point from each line:
    p3 = getSecondPoint(x1, y1, theta1)
    p4 = getSecondPoint(x2, y2, theta2)

    #Get the slope of both lines
    m1 = slope(x1, y1, p3[0], p3[1])
    m2 = slope(x2, y2, p4[0], p4[1])

    #Get the y-intercept of both lines
    b1 = findB(m1, x1, y1)
    b2 = findB(m2, x2, y2)

    #Get stronghold X (where the lines intersect)
    Xf = findStrongholdX(m1, m2, b1, b2)
    Yf = findStrongholdY(Xf, m1, b1)

    return Yf, Xf

#Get the input values from the user
x1 = getInputNumber(prompt1)
z1 = getInputNumber(prompt2)
theta1 = getInputNumber(prompt3)
x2 = getInputNumber(prompt4)
z2 = getInputNumber(prompt5)
theta2 = getInputNumber(prompt6)




#Convert the minecraft angles to the standard angles in math
theta1 = convertToStandardAngle(theta1)
theta2 = convertToStandardAngle(theta2)

#Convert the minecraft coordinates to standard coordinates.
x_s1, y_s1 = convertCoordsToStandard(x1, z1)
x_s2, y_s2 = convertCoordsToStandard(x2, z2)


#Note, investigate your B


#Test values for standard coordinates
#x_s1 = 3.0
#x_s2 = 16.8
#y_s1 = 0.0
#y_s2 = 0
#theta1 = 53.130102354156 
#theta2 = 111.8014094863518
#print(x1, "   ", x2)
X_sf, Z_sf = triangulate(x_s1, y_s1, theta1, x_s2, y_s2, theta2)
#X_sf, Y_sf = triangulate(x_s1, y_s1, theta1, x_s2, y_s2, theta2)
#X_mcf, Z_mcf = convertCoordsToMC(X_sf, Y_sf)

print("your stronghold is located at (", round(X_sf, 0), ", ", round(Z_sf, 0), ")")
#getSecondPointUnitTest()




#Unit Test Distance Formula
#distanceUnitTest()

#Unit Test Slope
#slopeUnitTest()
