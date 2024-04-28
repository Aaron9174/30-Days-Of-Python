########################################
#          EXERCISES - Level 3         #
#             Sets Practice            #
########################################

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f"The ages list is:\n{age}")
print(f"The length of the list is: {len(age)}")

ageSet = set(age)
print(f"The ages set is:\n{ageSet}")
print(f"The ages set length is: {len(ageSet)}")

print(f"The set has a lower length of {len(ageSet)} than the list length of {len(age)} because it removes duplicated entries.")

print(f"Explain the difference between the following data types: string, list, tuple, and set.")
print("String: A list of characters.")
print("List: A mutable and indexable list of items that can have duplicate items.")
print("Tuple: An immutable and indexable tuple of items that can have duplicate items.")
print("Set: An mutable and indexable set of items that cannot have duplicate items.")

teacherString = "I am a teacher and I love to inspire and teach people."
print(f"Practice string is:\n{teacherString}")
teacherStringSet = set(teacherString.split(" "))
print(f"The list of unique words in the practice string is {len(teacherStringSet)}")
