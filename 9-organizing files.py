# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:02:20 2019

@author: MooreN
"""

# shell utilities
import shutil, os, zipfile

os.chdir('C:\\Users\\MooreN\\r-work\\automateboring\\fake')

# copies with the same name
shutil.copy('foo.py', '.\\experiment')

# copies with a new name
shutil.copy('foo2.py', '.\\experiment\\foomanchu.py')

# copies a folder and everything beneath it
shutil.copytree('.\\experiment', '..\\quiz\\newfolder')

# moving files
shutil.move('..\\quiz\\newfolder\\foo.py', '..')

# move and rename
shutil.move('..\\quiz\\newfolder\\foomanchu.py', '..\\foobar.py')

# move can rename something without an extension, if there is no folder
shutil.move('..\\foobar.py', '..\\quiz\\newfolder\\bacon')

# folders must exist to move a file
shutil.move('..\\foo.py', 'C:\\nonsense\\eggs\\bacon')

# possible to delete single files and folders with os

# remove a file
os.unlink('path.py')

# remove an empty directory
os.rmdir('path')

# delete all files and folders
# !!!!! be careful !!!!!
shutil.rmtree('path')

# want to delete text files but actually there is a typo
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
        
# try this instead first to see what will be deleted with print()        
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
        
##### safe deletes with send2trash module
import send2trash
bacon_file = open('bacon.txt', 'w') # create a file
bacon_file.write('I love bacon')
bacon_file.close()
send2trash.send2trash('bacon.txt')
        
##### os.walk to walk through a directory structure
for foldername, subfolders, filenames in os.walk('C:\\Users\\mooren\\r-work\\automateboring'):
    print('The current folder is ' + foldername)
    
    for subfolder in subfolders:
        print('subfolder of ' + foldername + ': ' + subfolder) 
    for filename in filenames:
        print('file inside of ' + foldername + ': ' + filename) 
    print('')
        
##### compress files with zipfile
        
os.getcwd()
os.chdir('C:\\Users\\mooren\\r-work\\automateboring')

boring_zip = zipfile.ZipFile('automateboring.zip')

boring_zip.namelist()

some_info = boring_zip.getinfo('3-collatz.py')        

some_info.file_size

some_info.compress_size

'Uncompressed file is %sx larger!' % (round(some_info.file_size / some_info.compress_size, 2))

boring_zip.close()

# extracting from zip files


boring_zip = zipfile.ZipFile('automateboring.zip')

os.mkdir('C:\\Users\\mooren\\r-work\\automateboring\\boring')
os.chdir('C:\\Users\\mooren\\r-work\\automateboring\\boring')

boring_zip.extractall()

boring_zip.extract('3-collatz.py')        
        
boring_zip.close()
        
        
# creating and adding zip files

new_zipper = zipfile.ZipFile('new.zip', 'w') 

new_zipper.write('2-Flow Control.py', compress_type = zipfile.ZIP_DEFLATED)        

new_zipper.close()        

new_zipper = zipfile.ZipFile('new.zip', 'a') 

new_zipper.write('4-Practice Questions.py', compress_type = zipfile.ZIP_DEFLATED)        
        
new_zipper.close()            
        
        
     















   
        