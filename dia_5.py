# 1.
empty_list = []

# 2.
fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi', 'grape']

# 3.
print(len(fruits))

# 4. 
first = fruits[0]
middle = fruits[len(fruits) // 2]
last = fruits[-1]
print(first, middle, last)

# 5.
mixed_data_types = ['Carlos', 30, 1.75, 'Single', 'Madrid, Spain']

# 6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.
print(it_companies)

# 8. 
print(len(it_companies))

# 9.
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# 10. 
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. 
it_companies.append('Tesla')
print(it_companies)

# 12. 
it_companies.insert(len(it_companies)//2, 'Spotify')
print(it_companies)

# 13. 
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14.
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# 15.
print('Google' in it_companies)

# 16. 
it_companies.sort()
print(it_companies)

# 17.
it_companies.reverse()
print(it_companies)

# 18.
print(it_companies[:3])

# 19. 
print(it_companies[-3:])

# 20. 
length = len(it_companies)
if length % 2 == 0:
    print(it_companies[length//2 - 1 : length//2 + 1])
else:
    print(it_companies[length//2])

# 21. 
del it_companies[0]
print(it_companies)

# 22. 
mid = len(it_companies) // 2
del it_companies[mid]
print(it_companies)

# 23. 
it_companies.pop()
print(it_companies)

# 24.
it_companies.clear()
print(it_companies)

# 25. 
del it_companies

# 26. 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
tech_stack = front_end + back_end
print(tech_stack)

# 27.
full_stack = tech_stack.copy()
index_redux = full_stack.index('Redux')
full_stack[index_redux+1:index_redux+1] = ['Python', 'SQL']
print(full_stack)

#part 2

# 1. Estudiantes edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted:", ages)
print("Min:", min(ages), "Max:", max(ages))
ages.append(min(ages))
ages.append(max(ages))
print("With Min/Max added:", ages)
median = (ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2
print("Median:", median)
average = sum(ages) / len(ages)
print("Average:", average)
range_ = max(ages) - min(ages)
print("Range:", range_)
print("Min-Average:", abs(min(ages) - average))
print("Max-Average:", abs(max(ages) - average))





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
];

# Middle country or countries
length = len(countries)
if length % 2 == 0:
    mid1 = countries[length // 2 - 1]
    mid2 = countries[length // 2]
    print("Middle countries:", mid1, "and", mid2)
else:
    middle = countries[length // 2]
    print("Middle country:", middle)


# Split countries list in half
half = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]


print("First half ({} countries):".format(len(first_half)), first_half)
print("Second half ({} countries):".format(len(second_half)), second_half)

# Unpack countries
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = country_list

print("First 3 countries:", first, second, third)
print("Scandic countries:", scandic_countries)

