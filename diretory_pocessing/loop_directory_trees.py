# -*- coding: utf-8 -*-
import os

for folderName, subfolders, filenames in os.walk(
        r'F:\Transsion\New market\latest version software checklist by country'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')
