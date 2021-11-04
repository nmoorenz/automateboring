# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:44:00 2019

@author: MooreN
"""

"""
Q:1. What is the function that creates Regex objects?

re.compile()

Q:2. Why are raw strings often used when creating Regex objects?

don't have to do so much excaping

Q:3. What does the search() method return?

finds the first match as a match object

Q:4. How do you get the actual strings that match the pattern from a Match object?

mo.group()

Q:5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', 
what does group 0 cover? Group 1? Group 2?

0 covers the whole thing, 1 is (\d\d\d) and 2 is (\d\d\d-\d\d\d\d)

Q:6. Parentheses and periods have specific meanings in regular expression syntax. 
How would you specify that you want a regex to match actual parentheses and period characters?

\( \) \.

Q:7. The findall() method returns a list of strings or a list of tuples of strings. 
What makes it return one or the other?

no groups means list, groups means tuple

Q:8. What does the | character signify in regular expressions?

or

re.compile(r'batman|superman')

Q:9. What two things does the ? character signify in regular expressions?

zero or one characters, or nongreedy matching

Q:10. What is the difference between the + and * characters in regular expressions?

* is zero or more, + is one or more of a group

Q:11. What is the difference between {3} and {3,5} in regular expressions?

match 3 characters, or match between 3 and 5 characters

Q:12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

digit, word, space

Q:13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

not a digit, not a word, not a space

Q:14. How do you make a regular expression case-insensitive?

re.IGNORECASE or re.I as the second argument

Q:15. What does the . character normally match? 
What does it match if re.DOTALL is passed as the second argument to re.compile()?

normally matches anything except newline, then matches newline

Q:16. What is the difference between these two: .* and .*?

match anything, but also maybe nongreedy

Q:17. What is the character class syntax to match all numbers and lowercase letters?

[0-9a-z]

Q:18. If numRegex = re.compile(r'\d+'), 
what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

'X drummers, X pipers, five rings, X hens'

Q:19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

write comments in re.compile()

Q:20. How would you write a regex that matches a number with commas for every three digits? 
It must match the following:

'42'

'1,234'

'6,368,745'

but not the following:

'12,34,567' (which has only two digits between the commas)

'1234' (which lacks commas)

Q:21. How would you write a regex that matches the full name of someone 
whose last name is Nakamoto? You can assume that the first name that comes 
before it will always be one word that begins with a capital letter. 
The regex must match the following:

'Satoshi Nakamoto'

'Alice Nakamoto'

'Robocop Nakamoto'

but not the following:

'satoshi Nakamoto' (where the first name is not capitalized)

'Mr. Nakamoto' (where the preceding word has a nonletter character)

'Nakamoto' (which has no first name)

'Satoshi nakamoto' (where Nakamoto is not capitalized)

Q:22. How would you write a regex that matches a sentence where the first 
word is either Alice, Bob, or Carol; the second word is either eats, pets, 
or throws; the third word is apples, cats, or baseballs; and the sentence 
ends with a period? This regex should be case-insensitive. 
It must match the following:

'Alice eats apples.'

'Bob pets cats.'

'Carol throws baseballs.'

'Alice throws Apples.'

'BOB EATS CATS.'

but not the following:

'Robocop eats apples.'

'ALICE THROWS FOOTBALLS.'

'Carol eats 7 cats.'

"""

import re

# Q18
numRegex = re.compile(r'\d+')

numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')

# Q20

comma_regex = re.compile(r'^\d{1,3}(,\d{3})*$')

comma_regex.search('42')

comma_regex.search('1,234')

comma_regex.search('6,368,745')

comma_regex.search('12,34,567') == None

comma_regex.search('1234') == None

# Q21 

Nakamoto_regex = re.compile(r'^[A-Z]\w+ Nakamoto$')

q21_1 = 'Satoshi Nakamoto'
q21_2 = 'Alice Nakamoto'
q21_3 = 'Robocop Nakamoto'

q21_4 = 'satoshi Nakamoto'
q21_5 = 'Mr. Nakamoto'
q21_6 = 'Nakamoto'
q21_7 = 'Satoshi nakamoto'

Nakamoto_regex.search(q21_1)
Nakamoto_regex.search(q21_2)
Nakamoto_regex.search(q21_3)
Nakamoto_regex.search(q21_4) == None
Nakamoto_regex.search(q21_5) == None
Nakamoto_regex.search(q21_6) == None
Nakamoto_regex.search(q21_7) == None

# Q22

weird_regex = re.compile(r'^(Alice|Bob|Carol) (eats|pets|throws) (baseballs|cats|apples)\.$', re.I)

weird_regex.search('Alice eats apples.')
weird_regex.search('Bob pets cats.')
weird_regex.search('Carol throws baseballs.')
weird_regex.search('Alice throws Apples.')
weird_regex.search('BOB EATS CATS.')
weird_regex.search('Robocop eats apples.') == None
weird_regex.search('ALICE THROWS FOOTBALLS.') == None
weird_regex.search('Carol eats 7 cats.') == None





