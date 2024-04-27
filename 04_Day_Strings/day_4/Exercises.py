########################################
#               EXERCISES              #
#          String Manipulation         #
########################################

import math


string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
string5 = "{} {} {} {}".format(string1, string2, string3, string4)

string6 = "Coding"
string7 = "For"
string8 = "All"
string9 = "%s %s %s" %(string6, string7, string8)

# Using simple string formatting
print("########################################")
print("#    Using simple string formatting    #")
print("########################################")
challenge = string9
print("Challenge: {}".format(challenge))
print("Challenge Name length: {}".format(len(challenge)))

# Upper-case and lower-case utilities
print("########################################")
print("# Upper-case and lower-case utilities  #")
print("########################################")
challengeUpper = challenge.upper()
print("Challenge Upper: {}".format(challengeUpper))
challengeLower = challenge.lower()
print("Challenge Lower: {}".format(challengeLower))
challengeCap = challenge.capitalize();
print("Challenge capitalize: {}".format(challengeCap))
challengeTitle = challenge.title();
print("Challenge title: {}".format(challengeTitle))
challengeSwapCase = challenge.swapcase();
print("Challenge swapcase: {}".format(challengeSwapCase))

# Substrings
print("########################################")
print("#              Substrings              #")
print("########################################")
challengeNoCode = challenge[7:len(challenge)]
print("Company with first word removed: {}".format(challengeNoCode))
foundCode = challenge.find("Code")
print("Find 'Code': {}".format(foundCode))
print("Challenge: {}".format(challenge))
replaceCodeWithPython = challenge.replace("Coding", "Python")
print("replaceCodeWithPython: {}".format(replaceCodeWithPython))
splitOnSpace = challenge.split(" ")
print("splitOnSpace: {}".format(splitOnSpace))
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitCompanies = companies.split(",")
print("splitCompanies: {}".format(splitCompanies))
charAtIndexTen = challenge[10]
print("charAtIndexTen: {}".format(charAtIndexTen))

# Making acronyms
print("########################################")
print("#           Making acronyms            #")
print("########################################")
challenge2 = "Python For Everyone"
print("Make an an acronym from '{}'".format(challenge2))
def makeAcronym(string):
    upperList = [l for l in string if l.isupper()] # Get a list of all capital letters in a string
    return "".join(upperList)
print("Acronym: {}".format(makeAcronym(challenge2)))
print("Make an an acronym from '{}'".format(challenge))
print("Acronym: {}".format(makeAcronym(challenge)))

# Substring index utility functions
print("########################################")
print("#  Substring index utility functions   #")
print("########################################")
indexOfC = challenge.index('C')
print(f"First index of 'C' in {challenge} is {indexOfC}")
indexOfF = challenge.index('F')
print(f"First index of 'F' in {challenge} is {indexOfF}")
lastIndexOfl = challenge.rfind('l')
print(f"Last index of 'l' in {challenge} is {lastIndexOfl}")
challenge3 = "You cannot end a sentence with because because because is a conjuction"
firstBecauseIndex = challenge3.index("because")
print(f"Find the index of the first word in '{challenge3}'")
print(f"The index is {firstBecauseIndex}")
lastBecauseIndex = challenge3.rfind("because")
print(f"Find the index of the last word in '{challenge3}'")
print(f"The index is {lastBecauseIndex}")
splitOutBecauseWord = challenge3.replace("because ", "")
print(f"Remove the word because from '{challenge3}'")
print(f"The word 'because' removed: '{splitOutBecauseWord}'")

# Start and ends with utilities
print("########################################")
print("#    Start and ends with utilities     #")
print("########################################")
startWithCoding = challenge.startswith("Coding")
print(f"Does '{challenge}' start with 'Coding'? {startWithCoding}")
endWithCoding = challenge.endswith("Coding")

# Whitespace stripping
print("########################################")
print("#        Whitespace stripping          #")
print("########################################")
print(f"Does '{challenge}' end with 'Coding'? {endWithCoding}")
extraWhiteSpaceChallenge = "   Coding For All      "
print(f"Trim the following string of whitespace beginning and end whitespace: {extraWhiteSpaceChallenge}")
trimWhiteSpace = extraWhiteSpaceChallenge.strip(" ")
print(f"Stripped version: {trimWhiteSpace}")

# Check if valid variable
print("########################################")
print("#       Check if valid variable        #")
print("########################################")
var1String = "30DaysOfPyton"
var2String = "thirty_days_of_python"
print(f"Is the variable1 string '{var1String}' a valid python variable? {var1String.isidentifier()}")
print(f"Is the variable2 string '{var2String}' a valid python variable? {var2String.isidentifier()}")

# List joining
print("########################################")
print("#            List joining              #")
print("########################################")
pythonLibraryList = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(f"Join the list {pythonLibraryList} with hashtags")
joinedLibraryList = "#".join(pythonLibraryList)
print(f"Joined list: {joinedLibraryList}")

# Newline escape character
print("########################################")
print("#      Newline Escape Character        #")
print("########################################")
sentence1 = "I am enjoying this challenge"
sentence2 = "I just wonder what is next"
print(f"Join the two sentences '{sentence1}' and '{sentence2}' with a new line")
sentence3 = sentence1 + "\n" + sentence2
print(f"Joined sentenced:\n{sentence3}")

# Tab practice 
print("########################################")
print("#             Tab Practice             #")
print("########################################")
header = "Name\tAge\tCountry\t\tCity"
data = "Aaron\t500\tUnited States\tOrlando"
print(f"{header}\n{data}")

# String formatting to display results
print("########################################")
print("#       Display area of a circle       #")
print("########################################")
radius = 10
area = math.pi * radius ** 2
print(f"The area of a circle with a radius {radius} is {area:0.0f} meters square")

# Final practice
print("########################################")
print("#            Final practice            #")
print("########################################")
num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")