########################################
#             EXERCISE TWO             #
#          Area of a Triangle          #
########################################

base = input("Enter base: ")
height = input("Enter height: ")

def calculateAreaOfTriangle(base, height):
    return (base * height) / 2

area = calculateAreaOfTriangle(float(base), float(height))

print("The area of the triangle is " + str(area))