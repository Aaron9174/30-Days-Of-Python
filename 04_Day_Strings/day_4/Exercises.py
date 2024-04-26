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

company = string9
print("Company name: {}".format(company))
print("Company name length: {}".format(len(company)))
company = company.upper()
print("Company name (upper): {}".format(company))
company = company.lower()
print("Company name (lower): {}".format(company))