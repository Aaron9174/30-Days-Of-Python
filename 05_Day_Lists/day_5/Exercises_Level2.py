########################################
#          EXERCISES - Level 2         #
#             List Practice            #
########################################

# Utility functions
def isEven(agesListSize):
    return agesListSize % 2 == 0
def findMedian(ages):
    middleIndex = len(ages) // 2
    if (isEven(len(ages))):
        return (ages[middleIndex] + ages[middleIndex-1]) / 2
    else:
        return ages[middleIndex]
def findMean(ages):
    total = 0
    for age in ages:
        total += age
    return total / len(ages)


# A list of 10 student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort and find the min & max ages
ages.sort()
maxAge = max(ages)
minAge = min(ages)

# Add the min & max ages to the list
ages.append(maxAge)
ages.append(minAge)

# Find the mean, medium, and mode
medianAge = findMedian(ages)
meanAge = findMean(ages)
rangeAge = maxAge - minAge

# Minimum and maximum compared to average
minToAverage = abs(minAge - meanAge)
maxToAverage = abs(maxAge - meanAge)
print(f"Minimum compared to average: {minToAverage}")
print(f"Maximum compared to average: {maxToAverage}")

# List of countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Divide country list into two different lists
middleIndex = len(countries) // 2
if (not isEven(len(countries))):
    countrySet1 = countries[0:middleIndex]
    countrySet2 = countries[middleIndex:]
else:
    countrySet1 = countries[0:middleIndex+1]
    countrySet2 = countries[middleIndex+1:]
print("Country Set 1")
print("###############")
print(f"{countrySet1}")
print("Country Set 2")
print("###############")
print(f"{countrySet2}")

otherCountries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
china, russia, usa, *scandic = otherCountries
print(f"China: {china}\nRussia: {russia}\nUSA: {usa}\nScandic Countries: {scandic}")