########################################
#               EXERCISES              #
#          String Manipulation         #
########################################

string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
string5 = "{} {} {} {}".format(string1, string2, string3, string4)

string6 = "Coding"
string7 = "For"
string8 = "All"
string9 = "%s %s %s" %(string6, string7, string8)

challenge = string9
print("Challenge: {}".format(challenge))
print("Challenge Name length: {}".format(len(challenge)))
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
challenge2 = "Python For Everyone"
print("Make an an acronym from '{}'".format(challenge2))
def makeAcronym(string):
    upperList = [l for l in string if l.isupper()] # Get a list of all capital letters in a string
    return "".join(upperList)
print("Acronym: {}".format(makeAcronym(challenge2)))
print("Make an an acronym from '{}'".format(challenge))
print("Acronym: {}".format(makeAcronym(challenge)))
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
startWithCoding = challenge.startswith("Coding")
print(f"Does '{challenge}' start with 'Coding'? {startWithCoding}")
endWithCoding = challenge.endswith("Coding")
print(f"Does '{challenge}' end with 'Coding'? {endWithCoding}")