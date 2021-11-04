# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:05:42 2019

@author: MooreN
"""

##### webbrowser module (standard)

import webbrowser
import os

webbrowser.open('http://www.google.com')

##### requests module (install)

import requests

my_url = 'https://automatetheboringstuff.com/files/rj.txt'

res = requests.get(my_url)

type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])

nonsense = 'https://automatetheboringstuff.com/does_not_exist'

res = requests.get(nonsense)

# check for good url
res.raise_for_status()

# maybe we want to use try and except instead

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
    
##### download files to drive

os.chdir('C:\\Users\\mooren\\r-work\\automateboring')

res = requests.get(my_url)

res.raise_for_status()
play_file = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    play_file.write(chunk)
    
play_file.close()

##### HTML

import requests
import bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
type(no_starch_soup)

"""
Selector passed to the select() method
Will match...

soup.select('div')
All elements named <div>

soup.select('#author')
The element with an id attribute of author

soup.select('.notice')
All elements that use a CSS class attribute named notice

soup.select('div span')
All elements named <span> that are within an element named <div>

soup.select('div > span')
All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')
All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')
All elements named <input> that have an attribute named type with value button
"""

import os
os.chdir('C:\\Users\\mooren\\r-work\\automateboring')

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file.read())
auth_elems = example_soup.select('#author')
type(auth_elems)                            
len(auth_elems)

type(auth_elems[0])
auth_elems[0].getText()
str(auth_elems[0])
auth_elems[0].attrs

p_elems = example_soup.select('p')

str(p_elems[0])
p_elems[0].getText()
str(p_elems[1])
p_elems[1].getText()
str(p_elems[2])
p_elems[2].getText()

span_soup = bs4.BeautifulSoup(open('example.html'))
span_elem = span_soup.select('span')[0]
str(span_elem)
span_elem.get('id')
span_elem.get('nonsense_') == None
span_elem.attrs
