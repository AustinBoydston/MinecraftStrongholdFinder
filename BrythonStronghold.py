# Stronghold Locator App
# Author: Austin Boydston
# Description: This program takes in the coordinates and angle of
# two different eye of ender throws and calculates the location of 
# the stronghold.
from browser import document
import math as m





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
    m = slope(x1, y1, x2, y2)

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
    
def findBUnitTest():
    x = 2
    y = 3
    m = 1
    b_1 = findB(m, x, y)
    #projected b 
    b = 1
    if b_1 == b:
        print("Find B unit test 1 passed")
    else:
        print("Find B unit test 1 failed")
    
    x = -2
    y = 3
    m = 2
    b_2 = findB(m, x, y)
    #projected b = 7
    b = 7
    if b_2 == b:
        print("Find B unit test 2 passed")
    else:
        print("Find B unit test 2 failed")

#Unit test find stronghold x unit test
def findStrongholdXUnitTest():
    m1 = 2
    b1 = 1
    m2 = 3
    b2 = -2
    x_1 = findStrongholdX(m1, m2, b1, b2)

    #Expected x value = 3
    x = 3
    if x_1 == x:
        print("Find Stronghold X unit test 1 passed")
    else:
        print("Find Stronghold X unit test 1 failed")

    m1 = -40
    m2 = 10
    b1 = -3
    b2 = -7
    x_2 = findStrongholdX(m1, m2, b1, b2)
    #Expected x value = 4/50
    x = 4/50
    if x_2 == x:
        print("Find Stronghold X Unit Test 2 Passed")
    else:
        print("Find Stronghold X Unit Test 2 Failed")
    return 0


def findStrongHoldYUnitTest():
    b = 4
    m = 2
    x = 2
    y_1 = findStrongholdY(x, m, b)
    #Expected y value = 8
    y = 8

    if y_1 == y:
        print("Find Stronghold Y Unit Test 1 Passed")
    else:
        print("Find Stronghold Y Unit Test 1 Failed")
    
    b = 15
    m = -.5
    x = 30
    y_2 = findStrongholdY(x, m, b)
    #Expected y value = 0
    y = 0
    if y_2 == y:
        print("Find Stronghold Y Unit Test 2 Passed")
    else:
        print("Find Stronghold Y Unit Test 2 Failed")

    
#Convert to standard angle unit test
def convertToStandardAngleUnitTest():
    theta_1 = -135
    #Expected value for theta
    theta = 135
    theta_1 = convertToStandardAngle(theta_1)
    print(theta_1, ", ", theta)
    if theta_1 == theta:
        print("Convert To Standard Angle Unit Test 1 Passed")
    else:
        print("Convert To Standard Angle Unit Test 1 Failed")
       
        
    theta_2 = 58
    #expected value
    theta = 302
    theta_2 = convertToStandardAngle(theta_2)
    print(theta_2, ", ", theta)
    if theta == theta_2:
        print("Convert To Standard Angle Unit Test 2 Passed")
    else:
        print("Convert To Standard Angle Unit Test 2 Failed")

def convertCoordsToStandardUnitTest():
    coord1_x = 2
    coord2_z = 4
    x_1, y_1  = convertCoordsToStandard(coord1_x, coord2_z)
    #Expected Values
    x = 4
    y = 2
    if x == x_1 and y == y_1:
        print("Convert Coords To Standard Unit Test 1 Passed")
    else:
        print("Convert Coords To Standard Unit Test 1 Failed")


def convertCoordsToMCUnitTest():
    x_1 = 3
    y_1 = 7

    x_1, z_1 = convertCoordsToMC(x_1, y_1)
    #Expected Values
    x = 3
    z = 7
    if x == x_1 and z == z_1:
        print("Convert Coords To MC Unit Test 1 Passed")
    else:
        print("Convert Coords To MC Unit Test 1 Failed")
    
    x_2 = -17
    y_2 = 29
    x_2, z_2 = convertCoordsToMC(x_2, y_2)
    #Expected Values
    x = -17
    z = 29
    if x == x_2 and z == z_2:
        print("Convert Coords To MC Unit Test 2 Passed")
    else:
        print("Convert Coords To MC Unit Test 2 Failed")

def triangulateUnitTest():
    x_s1 = 3.0
    x_s2 = 16.8
    y_s1 = 0.0
    y_s2 = 0
    theta1 = 53.130102354156 
    theta2 = 111.8014094863518
    #print(x1, "   ", x2)
    X_sf, Z_sf = triangulate(x_s1, y_s1, theta1, x_s2, y_s2, theta2)
    #Expected Value
    X = 12.0
    Z = 12.0
    if round(X_sf, 0) == X and round(Z_sf, 0) == Z:
        print("Triangulate Unit Test Passed")
    else:
        print("Triangulate Unit Test Failed")
        print("Expected: X = ", X, "Z = ", Z, "  But found X = ", X_sf, " Z = ", Z_sf)

#########################################End Unit Test Definitions########################## 





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
    
    if theta < 0:
        theta = -theta
    else:
        theta = (theta / 180) 
        theta = 1 - theta
        theta = (theta * 180) + 180
    return theta


#convert the coordinates to standard cartesian coordinates.
def convertCoordsToStandard(x,z):
    return z, x


def convertCoordsToMC(x, y):
    return x, y


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


########################## End Function Definitions ########################


#Get the input values from the user
x1 = document["input1"].value
z1 = document["input2"].value
theta1 = document["input3"].value
x2 = document["input4"].value
z2 = document["input5"].value
theta2 = document["input6"].value




#Convert the minecraft angles to the standard angles in math
theta1 = convertToStandardAngle(theta1)
theta2 = convertToStandardAngle(theta2)

#Convert the minecraft coordinates to standard coordinates.
x_s1, y_s1 = convertCoordsToStandard(x1, z1)
x_s2, y_s2 = convertCoordsToStandard(x2, z2)






X_sf, Z_sf = triangulate(x_s1, y_s1, theta1, x_s2, y_s2, theta2)

print("your stronghold is located at (", round(X_sf, 0), ", ", round(Z_sf, 0), ")")




#################Call Unit Tests##############################

#getSecondPointUnitTest()

#Unit Test Distance Formula
#distanceUnitTest()

#Unit Test Slope
#slopeUnitTest()


#Unit test findB
#findBUnitTest()

#Unit Test Find Stronghold X
#findStrongholdXUnitTest()

#Unit Test Find Stronghold Y
#findStrongHoldYUnitTest()

#Unit Test Convert To Standard Angle
#convertToStandardAngleUnitTest()

#Unit Test Convert Standard Coordinates to Minecraft Coordinates
#convertCoordsToMCUnitTest()

#Unit Test Triangulate
#triangulateUnitTest()