# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:18:01 2019

@author: MooreN

Project: Backing Up a Folder into a ZIP File

Copy an entire folder and its contents into a ZIP file whose 
filename increments automatically

"""

import zipfile
import os

def backup_to_zip(folder):
    # backup the contents of "folder" to a zip file
    
    # absolute reference
    folder = os.path.abspath(folder) 
    
    # figure filename based on previous zips
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
        
    # create the zip file
    print('Creating %s...' % (zip_filename))
    print('Saving in %s...' % (os.getcwd()))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    # walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        
        # add current folder to zip file
        backup_zip.write(foldername)
        
        # add all files in this folder
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # don't backup zip files
            backup_zip.write(os.path.join(foldername, filename)) 
        
    backup_zip.close()
    
    print('Done.')
    
    
backup_to_zip('C:\\automateboring')