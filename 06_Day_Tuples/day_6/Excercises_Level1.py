########################################
#          EXERCISES - Level 1         #
#            Tuple Practice            #
########################################

emptyTuple = ()
brothers = ("Andrew", "Christian", "Cory", "Mikey")
print(f"Brothers tuple is {brothers}")
sisters = ("Christina",)
print(f"Sister tuple is {sisters}")
siblings = brothers + sisters
print(f"Siblings tuple is {siblings}")
numOfSiblings = len(siblings)
print(f"numOfSiblings is {numOfSiblings}")
listFamily = list(siblings)
listFamily.append("Janet")
listFamily.append("Mike")
family = tuple(listFamily)
print(f"Family tuple is {family}")
