########################################
#          EXERCISES - Level 2         #
#            Tuple Practice            #
########################################

# Utility Functions
def isEven(number):
    return number % 2 == 0

print("########################################")
print("#            Family Example            #")
print("########################################\n")
family = ("Andrew", "Christian", "Cory", "Mikey", "Christina", "Janet", "Mike")
print(f"Family tuple is {family}")
brothers = family[0:4]
parents = family[-2:]
print(f"Brothers tuple is {brothers}")
print(f"Parents tuple is {parents}")

print("\n########################################")
print("#            Fruits Example            #")
print("########################################\n")
fruits = ("Banana", "Pineapple", "Strawberry", "Blueberry", "Kiwi")
vegetables = ("Carrots", "Broccoli", "Asparagus", "Green Beans", "Cauliflower", "Raddish")
animalProducts = ("Milk", "Lard", "Steak", "Pork Loin", "Butter")
foodStuffTp = fruits + vegetables + animalProducts
print(f"Food stuff tuple is:\n{foodStuffTp}\n")

foodStuffIt = foodStuffTp
foodStuffIt = list(foodStuffIt)
middleIndex = len(foodStuffIt) // 2
if (isEven(len(foodStuffIt))):
    foodStuffIt = foodStuffIt[0:middleIndex-1] + foodStuffIt[middleIndex+1:]
else:
    foodStuffIt = foodStuffIt[0:middleIndex] + foodStuffIt[middleIndex+1:]
print(f"Food stuff list without middle items is:\n{foodStuffIt}\n")

CUT_ITEMS_AMOUNT = 3
foodStuffIt = foodStuffIt[CUT_ITEMS_AMOUNT:-CUT_ITEMS_AMOUNT]
print(f"Cut the first three and last three food items out. The list now is:\n{foodStuffIt}\n")
del foodStuffTp

print("\n########################################")
print("#            Nordic Example            #")
print("########################################\n")
nordicCountries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print(f"Nordic countries {nordicCountries}")
isEstoniaNordic = "Estonia" in nordicCountries
isIcelandNordic = "Iceland" in nordicCountries
print(f"Is Estonia nordic? {isEstoniaNordic}")
print(f"Is Iceland nordic? {isIcelandNordic}")
print()
