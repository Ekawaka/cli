# regular expressions

import re

pattern = re.compile('^Hello')

#result = pattern.search('Hello world')

#print(result)

#result = pattern.finditer('Hello world')
#print(result)

#result = pattern.sub('Hi', 'Hello world, Hello, Kenya')

#print(result)

#(?)
#\d -> 0, 9
#\w -> 0-9, a-z, A-Z
#\s -> whitespace character
#[]
#
# *
#

#text = "This is my phone number 111-111-1111"

#pattern = r"\d{3}-\d{3}-\d{4}"

#result = re.search(pattern, text)

#print(result)

# define a regex pattern for the phone number +254-234-098-134"

text = "phone number +254-234-098-134"

pattern = r"\+\d{3}-\d{3}-\d{3}-\d{3}"            

result = re.search(pattern, text)

print(result)
