########################################
#          EXERCISES - Level 1         #
#             List Practice            #
########################################

########################################
#           Utility Functions          #
########################################
def calculateMiddleIndex(list):
    return len(list) // 2
def calculateLastIndex(list):
    return len(list) - 1


print("########################################")
print("#            Declaring Lists           #")
print("########################################\n")

list = []
list = ["Ahsoka", "Kratos", "Bam", "Christopher", "Aaron", "Ryan"]
print(f"Starting list {list}")
listLen = len(list)
print(f"Length of the starting list: {listLen}")

print("\n")

print("########################################")
print("#           Practice Indexing          #")
print("########################################\n")

firstIndex = 0
middleIndex = calculateMiddleIndex(list)
lastIndex = calculateLastIndex(list)
print(f"First Index\tMiddle Index\tLast Index")
print(f"{list[firstIndex]}\t\t{list[middleIndex]}\t{list[lastIndex]}")

print("\n")

print("########################################")
print("#           Practice Indexing          #")
print("########################################\n")
mixed_data_types = ["Aaron", 600, 170.18, False, "666 Devil Street"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(f"Tech Companies: {it_companies}")
print(f"Number of Tech Companies: {len(it_companies)}")
firstIndex = 0
middleIndex = calculateMiddleIndex(it_companies)
lastIndex = calculateLastIndex(it_companies)
print(f"\nFirst Company\tMiddle Company\tLast Company")
print(f"{it_companies[firstIndex]}\t{it_companies[middleIndex]}\t\t{it_companies[lastIndex]}")

print("\n")

print("########################################")
print("#           List Manipulation          #")
print("########################################\n")
facebookIndex = it_companies.index("Facebook")
it_companies[facebookIndex] = "Meta"
print(f"Facebook is now meta.\nUpdating list...")
print(f"New list: {it_companies}")
print(f"Adobe is a cool company. Lets add it.\nUpdating list...")
it_companies.append("Adobe")
print(f"New list: {it_companies}")
print(f"Tesla should be in the list. Inject it into the middle.\nUpdating list...")
it_companies.insert(middleIndex, "Tesla")
print(f"New list: {it_companies}")
print(f"Lets practice updating list contents. Change 'Apple' to 'APPLE'!\nUpdating list...")
appleIndex = it_companies.index("Apple")
it_companies[appleIndex] = it_companies[appleIndex].upper()
print(f"New list: {it_companies}")
print(f"Join the companies together int oa string with the delimiter '#; '")
weirdCompanyString = "#; ".join(it_companies)
print(f"Weird company string '{weirdCompanyString}'")
googleExists = "Google" in it_companies
print(f"Does Google exist in {it_companies}? {googleExists}")
sortedCompanyList = it_companies.copy()
sortedCompanyList.sort()
print(f"Sorted company list {sortedCompanyList}")
reverseSortedCompanyList = it_companies.copy()
reverseSortedCompanyList.sort(reverse=True)
print(f"Reverse sorted company list {reverseSortedCompanyList}")
print(f"The first three companies were cornered out of the market.\nUpdating list...")
marketAdjustmentCompanies = it_companies[3:len(it_companies)]
print(f"New list: {marketAdjustmentCompanies}")
print(f"The following companies have changed their customer bases.\nUpdating list...")
customerBaseDeltaCompanies = it_companies[0:len(it_companies)-3]
print(f"New list: {customerBaseDeltaCompanies}")
middleIndex = len(it_companies) // 2
middleSelectionStart = middleIndex - 1
middleSelectionEnd = middleIndex + 2
print(f"My favorite companies will now be calculated.\nUpdating list...")
favoriteCompanies = it_companies[0:middleSelectionStart] + it_companies[middleSelectionEnd:len(it_companies)]
print(f"New list: {favoriteCompanies}")
removeFirstCompany = it_companies[1:]
print(f"Remove first company for cheating the market {removeFirstCompany}")
removeMiddleCompany = it_companies[0:middleIndex] + it_companies[middleIndex+1:]
print(f"Remove middle company for cheating the market {removeMiddleCompany}")
removeLastCompany = it_companies[0:(len(it_companies)-1)]
print(f"Remove last company for cheating the market {removeLastCompany}")
it_companies.clear()
print(f"Companies are all caught cheating. They will be cleansed from the market.\nUpdating list...")
print(f"New list: {it_companies}")
print(f"Destroying list forever.\nUpdating list...")
del it_companies
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
all_in = front_end + back_end
full_stack = all_in.copy()
print(f"Full stack developer needs to have proficiency in {full_stack} languages")
reduxIndex = full_stack.index("Redux") + 1
full_stack.insert(reduxIndex, "Python")
reduxIndex += 1
full_stack.insert(reduxIndex, "SQL")
print("Two additional languages certainly help.\nUpdating list...")
print(f"New list: {full_stack}")
print("\n")