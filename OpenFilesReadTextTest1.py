import string
##f = open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') 
##print f.name
##f.close()
##    
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    f_contents = f.read()
##    print (f_contents)
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    f_contents = f.read(550)
##    print (f_contents)
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    size_to_read = 10
##    f_contents = f.read(size_to_read)
##    while len(f_contents)> 0:
##        print (f_contents, '**')
##        f_contents = f.read(size_to_read)
##
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    size_to_read = 10
##    f_contents = f.read(size_to_read)
##    print(f.tell())

with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print (f_contents, '**')
    f.seek(5)
    f_contents = f.read(size_to_read)
    print (f_contents, '**')
     
##        
##
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    f_contents = f.readlines()
##    print f_contents    
##    
##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    f_contents = f.readline()
##    print (f_contents, end='')

##with open(r"C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt", 'r') as f:
##    for line in f:
##        print(line)
##
##        

    

