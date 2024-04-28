########################################
#          EXERCISES - Level 1         #
#             Sets Practice            #
########################################

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"IT companies set is:\n{it_companies}")
print(f"\nThere are a total of {len(it_companies)} IT companies in the set.")
it_companies.add("Twitter")
print(f"Add 'Twitter' to the IT companies set. Updating set...\n{it_companies}")
other_it_companies = {"Adobe", "Tesla"}
it_companies.update(other_it_companies)
print(f"Add '{other_it_companies}' to the set. Updating set...\n{it_companies}")
it_companies.discard("Facebook")
print(f"Remove 'Facebook' from the set. Updating set...\n{it_companies}")
print(f"What is the difference between remove and discard?")
print(f"Remove will error if the element does not exist in the set while discard will do nothing.")