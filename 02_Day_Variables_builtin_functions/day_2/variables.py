#####################################
#         LEVEL 1 EXERCISE          #
#####################################

import math


print("Day 2: 30 Days of python programming")
first_name = "Aaron"
last_name = "Hebson"
full_name = first_name + " " + last_name
country = "United States"
city = "Palm Bay"
age = 28
year = 2024
is_married = False
is_true = True
is_light_on = False
bunny, dog, cat = "rabbit mom", ["Kratos", "Ahsoka"], "Bam"

#####################################
#         LEVEL 2 EXERCISE          #
#####################################

print("first_name type:")
print(type(first_name))
print("last_name type:")
print(type(last_name))
print("full_name type:")
print(type(full_name))
print("country type:")
print(type(country))
print("city type:")
print(type(city))
print("age type:")
print(type(age))
print("year type:")
print(type(year))
print("is_married type:")
print(type(is_married))
print("is_true type:")
print(type(is_true))
print("is_light_on type:")
print(type(is_light_on))
print("bunny type:")
print(type(bunny))
print("dog type:")
print(type(dog))
print("cat type:")
print(type(cat))

print("length of first_name:", len(first_name))
print("Length comparison (gt) of first_name and last_name")
print(len(first_name) > len(last_name))

num_one = 5
print("num_one:" + str(num_one))
num_two = 4
print("num_two:" + str(num_two))
total = num_one + num_two            #---> 9
print("total = " + str(total))
diff = num_one - num_two             #---> 1
print("diff = " + str(diff))
product = num_one * num_two          #---> 20
print("product = " + str(product))
division = num_one / num_two         #---> 1.25
print("division = " + str(division))
remainder = num_one % num_two        #---> 1
print("remainder = " + str(remainder))
exp = num_one ** num_two             #---> 625
print("exp = " + str(exp))
floor_division = num_one // num_two  #---> 1
print("floor_divison = " + str(floor_division))

# radius, area, and circumference of a circle
radius = 30
print("radius = " + str(radius))
area_of_circle = math.pi * (radius ** 2)
print("area_of_circle = " + str(area_of_circle))
circum_of_circle = 2 * math.pi * radius
print("circum_of_circle = " + str(circum_of_circle))

# Calculate dynamic radius
radius = input("Input a radius of a circle: ")
area_of_circle = math.pi * (float(radius) ** 2)
print("The radius is " + str(area_of_circle))

# Testing input function
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print("User Information")
print("================")
print("First Name: " + str(first_name))
print("Last Name: " + str(last_name))
print("Country: " + str(country))
print("Age: " + str(age))

# Python keywords
keywords = help("keywords")
print(keywords)
