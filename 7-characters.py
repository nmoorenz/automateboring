import re

# character classes in square brackets
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

# caret for negation
# not vowels
consonantReg = re.compile(r'[^aeiouAEIOU]')
consonantReg.findall('Robocop eats baby food. BABY FOOD.')

# caret and dollar for start and end of regex
begins_hello = re.compile(r'^Hello')
begins_hello.search('Hello world!')
begins_hello.search('world of Hello') == None
ends_digits = re.compile(r'\d+$')
ends_digits.search('magic 42')
ends_digits.search('42 is the answer') == None
whole_numbers = re.compile(r'^\d+$')
whole_numbers.search('12345678')
whole_numbers.search('789456+123') == None

# . character for wildcard
at_reg = re.compile(r'.at')
at_reg.findall('The cat in the hat sat on the flat mat')

# dot star to match everything (.*)
name_reg = re.compile(r'First Name: (.*) Last Name: (.*)')
reg_mo = name_reg.search('First Name: Bob Last Name: Taggart')
reg_mo.group(1)
reg_mo.group(2)

# greedy and non-greedy mode: ? non-greedy
non_greedy = re.compile(r'<.*?>')
non_greedy.search('<to serve man> for dinner>')
bit_greedy = re.compile(r'<.*>')
bit_greedy.search('<Serve a man> for dinner>')

# newlines with dot character
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

##############################################
# ? zero or one, * zero or more, + one or more
# {n} {n,} {,m} {n,m} preceding group counts
# {n,m}? *? +? non-greedy
# ^spam at the start, spam$ at the end
# . any character except newline
# \d, \w, \s digit, word, space
# \D, \W, \S not a digit, not a word, not a space
# [abc] character class [^abc] not that class [a-f] range for class

# case-insensitive re.IGNORECASE
robocop = re.compile(r'robocop', re.IGNORECASE)
robocop.search('robocop is part man part machine')
robocop.search('ROBOCOP IS NOT STUPID')

# substituting strings with sub(), use \1 for groups
agent_regex = re.compile(r'Agent \w+')
agent_regex.sub('CENSORED', 'Agent Alice should not have given those documents to Agent Bob')
agent_star = re.compile(r'Agent (\w)\w*')
agent_star.sub(r'\1****', 'Agent Alice told Agent Bob that Agent Carol knew Agent Dave was a double agent')

# re.VERBOSE for multiline regex expression with comments


