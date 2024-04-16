########################################
#            EXERCISE THREE            #
#        Perimeter of a Triangle       #
########################################

sideA = float(input("Enter side a: "))
sideB = float(input("Enter side b: "))
sideC = float(input("Enter side c: "))

def calculatePerimeterOfTriangle(sideA, sideB, sideC):
    return sum([sideA, sideB, sideC])

perimeter = calculatePerimeterOfTriangle(sideA, sideB, sideC)

print("The perimeter of the triangle is " + str(perimeter))
