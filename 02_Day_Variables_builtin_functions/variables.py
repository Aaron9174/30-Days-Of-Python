
#######################
# Variables in Python #
#######################

first_name = 'Aaron'
last_name = 'Hebson'
country = 'United States'
city = 'Palm Bay'
age = 28
is_married = False
skills = ['HTML', 'CSS', 'JS', 'TS', 'Vue.js', 'Bash']
person_info = {
    'firstname':'Aaron', 
    'lastname':'Hebson', 
    'country':'United States',
    'city':'Palm Bay'
    }

###############################################
# Printing the values stored in the variables #
###############################################

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

############################################
# Declaring multiple variables in one line #
############################################

first_name, last_name, country, age, is_married = 'Aaron', 'Hebson', 'Palm Bay', 28, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#########################
#  Checking data types  #
#########################

print(type("Aaron"))                                                # str
print(type("first_name"))                                           # str
print(type(10))                                                     # int
print(type(3.14))                                                   # float
print(type(1 + 1j))                                                 # complex
print(type([1,2,3,4]))                                              # list
print(type({"name": "Aaron", "age": 28, "is_married": 28}))         # dict
print(type((1,2)))                                                    # tuple
print(type(zip([1,2],[3,4])))                                       # set

###########################
#  Casting to data types  #
###########################

# int to float
print("int to float")
num_int = 10
print("num_int: ", num_int) #---> 10
num_float = float(num_int)  #---> 10.0

# float to int
print("float to int")
gravity = 9.81
print(int(gravity)) #---> 9

# int to str
print("int to str")
num_int = 10
print(num_int)           #---> 10
num_str = str(num_int)
print(num_str)           #---> "10"

# str to int or float
print("str to int or float")
num_str = "10"
print(num_int)           #---> "10"
num_str = float(num_str) #---> 10.0
print(num_int)
num_str = int(num_str)   #---> 10
print(num_int)
num_str = float(num_str) #---> 10.0
print(num_int)

# str to list
print("str to list")
first_name = "Aaron"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
