########################################
#            EXERCISE FOUR             #
#         All Remaining Areas          #
########################################

# Get area of a rectangle
import math


length = float(input("Input the length of the rectangle: "))
width = float(input("Input the width of the rectangle: "))
areaOfRectangle = length * width
print("Area of the rectangle: ", str(areaOfRectangle))

# Get area of a circle
radius = float(input("Enter the radius of a circle: "))
areaOfCircle = math.pi * (radius ** 2)
circumOfCircle = 2 * math.pi * radius
print("Area of the circle: ", str(areaOfCircle))
print("Circumference of the circle: ", str(circumOfCircle))

# Calculating the slope of a line
def calculateSlope(p1, p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])
# Calculates the eucledian distance of two points
def calculateEuclideanDistance(p1, p2):
    firstDimCalc = (p2[0] - p1[0]) ** 2
    secondDimCalc = (p2[1] - p1[1]) ** 2
    return math.sqrt(firstDimCalc + secondDimCalc)

## y = 2x - 2
savedSlope = 2
savedYIntercept = 1

# Example points
p1 = (2, 2)
p2 = (6, 10)
slope = calculateSlope(p1, p2)
print("Calculated slope: ", str(slope))
euclDistance = calculateEuclideanDistance(p1, p2)
print("Eucledian distance: ", str(euclDistance))
print("Slope comparison: ", savedSlope == slope)

# Calculate Y example
def calculateY(x):
    return x**2 + 6*x + 9
print("x^2 + 6x + 9")
print("------------")
print("Finding where y=0")
print("x=1: ", calculateY(1))
print("x=-3: ", calculateY(-3))

# String practice
python = "python"
dragon = "dragon"
print("The length of the string 'python' is greater than string 'dragon': ", len(python) > len(dragon))
onStr = "on"
onStringExists = (onStr in python) and (onStr in dragon)
print("The string " + onStr + " exists in the strings 'python' and 'dragon': ", onStringExists)
practiceSentence = "I hope this course is not full of jargon"
jargonStringExists = "jargon" in practiceSentence
print(practiceSentence)
print("The string 'jargon' exists in the practice sentence above above: ", jargonStringExists)
noStr = "no"
noStringExists = (noStr in python) and (noStr in dragon)
print("The string " + noStr + " exists in the strings 'python' and 'dragon': ", noStringExists)
pythonLenFloatStr = str(float(len(python)))
print("The string '" + python + "' length as float: " + pythonLenFloatStr)

# Function that tests that an integer is even
def evenChecker(num):
    if (num % 2 == 0):
        return True
    else:
        return False
print("Even Checker")
print("------------")
print("2 is even: " + str(evenChecker(2)))
print("21 is even: " + str(evenChecker(21)))
print("-12 is even: " + str(evenChecker(-12)))
print("20455561 is even: " + str(evenChecker(20455561)))

# Floor practice
floorResult = 7 // 3
testValue = int(2.7)
print("The floorResult of 7 // 3: ", floorResult)
print("The testValue of int(2.7): ", testValue)
print("Are they equal? ", testValue == floorResult)

# Type comparison
stringTypeTen = type("10")
intTypeTen = type(10)
print("The stringTypeTen type is " + str(stringTypeTen) + " and the integerTypeTen is " + str(intTypeTen))
print("Are they equal? ", stringTypeTen == intTypeTen)

# Integer conversion comparison
testVar1 = 9.8
testVar2 = 10
intTestVar = int(9.8)
print("The inputs are\ntestVar1: " + str(testVar1) + "\ntestVar2: " + str(testVar2) + "\ntestVar1 conversion to int is: ", intTestVar)
print("Does testVar2 equal the converted integer? ", testVar2 == intTestVar)

# Calculate total pay amount
numOfHours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is $" + str(numOfHours * rate))

# Calculate the number of seconds a person has lived
years = float(input("Enter the number of years you have lived: "))
DAYS_IN_A_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTE_IN_A_HOUR = 60
SECONDS_IN_A_MINUTE = 60
seconds = years * DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTE_IN_A_HOUR * SECONDS_IN_A_MINUTE
print("You have lived for " + str(seconds) + " seconds.")

# Print pretty table
table = [[1, 1, 1, 1, 1], [2, 1, 2, 4, 8], [3, 1, 3, 9, 27], [4, 1, 4, 16, 64], [5, 1, 5, 25, 125]]
def printRow(row):
    isEnd = False
    index = 0
    for value in row:
        isEnd = index == (len(row) - 1)
        if(isEnd):
            print(str(value))
        else:
            print(str(value) + " ", end="")
        index = index + 1
def printTable(table):
    for row in table:
        printRow(row)
printTable(table)