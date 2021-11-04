# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:58:17 2019

@author: MooreN
"""

import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phone_num_regex
print(phone_num_regex)

mo = phone_num_regex.search('My number is 415-555-4242')

mo

print('Phone number found: ' + mo.group())

# groups with parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

mo.group(0)

mo.group(1)

mo.group(2)

mo.group()

mo.groups()

# multi assignment
areacode, main_number = mo.groups()

print(areacode)
print(main_number)

# pipe operator, meaning OR

hero_regex = re.compile(r'Batman|Tina Fey')

mo1 = hero_regex.search('Batman and Tina Fey')
mo1.group()

mo2 = hero_regex.search('Tina Fey but not Batman')
mo2.group()

# match possibilities with a pipe
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = bat_regex.search('Batcopter lost the rotors')
mo.group()
mo.group(1)

# optional groups with ?
# match zero or one of the groups
bat_regex = re.compile(r'Bat(wo)?man')

mo_wo = bat_regex.search('The adventures of Batwoman')
mo_wo.group()

mo_ma = bat_regex.search('The boring adventures of Batman')
mo_ma.group()

# match zero or more of the groups
# any number of times with *
bat_star = re.compile(r'Bat(wo)*man')

mo_none = bat_star.search('The trips of Batman')
mo_none.group()

mo_one = bat_star.search('The loops of Batwoman')
mo_one.group()

mo_many = bat_star.search('The fancies of Batwowowowowowoman')
mo_many.group()

# match one or more with plus
bat_plus = re.compile(r'Bat(wo)+man')

mo_none = bat_plus.search('The trips of Batman')
mo_none.group()

mo_one = bat_plus.search('The loops of Batwoman')
mo_one.group()

mo_many = bat_plus.search('The fancies of Batwowowowowowoman')
mo_many.group()


# matching numbers of groups with {}
ha_regex = re.compile(r'(Ha){3}')

mo_ha = ha_regex.search('HaHaHa')
mo_ha.group()

mo_na = ha_regex.search('HaHa')
mo_na == None


# greedy greedy python (by default)
ha_greedy = re.compile(r'(Ha){3,5}')
mo_g = ha_greedy.search('HaHaHaHaHa')
mo_g.group()

ha_non = re.compile(r'(Ha){3,5}?')
mo_non = ha_non.search('HaHaHaHaHa')
mo_non.group()


# findall() method for all matches
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo_num = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo_num.group()

# as long as there are no groups in the regex
mo_fa = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
mo_fa # list of strings returned

phone_num_grp = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo_grp = phone_num_grp.findall('Cell: 415-555-9999 Work: 212-555-0000')
mo_grp # list of tuples returned


# character classes
# \d digits \s spaces \w word char
xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')























