# ------------------
'''
Identifiers - Định danh
\d any nunber
\D anything but a number
\s space
\D anything but a space
\w any character
\W anything but a character
. any character, except for a new line
\b the whitespace around words
\. a period

Modifiers:

{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of the string
^ Matching the beginning of a string
| either or ex: \d{1-3} | \w{5-6}
[] range or "variance" [A-Za-z] [1-5A-Z]
{x} expacting "x" amount

White Space Character

\n new Line
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET!:

. + * ? [ ] $ ^ ( ) | \


'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
# find all number length equal 1 -> 3
ages = re.findall(r'\d{1,3}',exampleString)
# find all words start equal UperCase
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}
x = 0;

for name in names:
    ageDict[name] = ages[x]
    x+=1

print(ageDict)