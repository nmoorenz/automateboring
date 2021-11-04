# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:59:28 2019

@author: MooreN
"""

# rename filenames from American dates mm-dd-yyyy to European yyyy-mm-dd

import shutil, os, re

os.chdir('C:\\Users\\mooren\\r-work\\automateboring\\boring')

# create regex to find american format
date_pattern = re.compile(r"""^(.*?)    # text before the date
((0|1)?\d)-                             # one or two digits for the month
((0|1|2|3)?\d)-                         # one or two digits for the day
((19|20)\d\d)                           # 1900 or 2000 years
(.*?)$                                  # any text after the date
""", re.VERBOSE)

# loop over the files in the working directory

for filename in os.listdir('.'):
    mo = date_pattern.search(filename)
    
    # if no date is found
    if mo == None:
        continue
    
    # get the different parts of the file name
    before_part = mo.group(1)
    month_part  = mo.group(2)
    day_part    = mo.group(4)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

    # form the European style filename
    euro_file = before_part + year_part + '-' + month_part + '-' + day_part + after_part

    # get the full absolute filepaths
    abs_working_dir = os.path.abspath('.')
    amer_file = os.path.join(abs_working_dir, filename)
    euro_file = os.path.join(abs_working_dir, euro_file)

    # rename the files
    #print('Renaming \n"%s" \nto \n"%s"\n' % (amer_file, euro_file))
    shutil.move(amer_file, euro_file)  # uncomment after testing

