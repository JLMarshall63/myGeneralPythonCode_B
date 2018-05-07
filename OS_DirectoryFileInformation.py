import os
from datetime import datetime
##print(dir(os))
##
##print(os.getcwd())

os.chdir(r'C:\University of Washington GIS\UOWSummer2017\GEOG565\PythonScripts/')
##print(os.getcwd())
##print(dir(os))
#print(os.listdir(dir))

for dirpath, dirnames, filenames in os.walk(r'C:\University of Washington GIS\UOWSummer2017\GEOG565\PythonScripts/'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
    
