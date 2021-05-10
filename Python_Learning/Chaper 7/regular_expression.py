import re

#REGular EXpression (REGEX) are descriptions for a pattern of text
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # REGEX Object #Pass desired pattern and store resulting Regex object
mo = phoneNumRegex.search('My number is 415-555-4242.') # Match Object #Call search method, and pass the string wanted to search for match
print('Phone number found: ' + mo.group())
