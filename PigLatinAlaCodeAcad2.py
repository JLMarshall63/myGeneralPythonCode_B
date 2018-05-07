try:  
    entry = ""    
    entry = raw_input("Enter an English word here: ")
    if len(entry) > 0 and entry.isalpha():
        entry2 = entry.lower()
        
        firstLetter = entry2[0]
        pyg = "ay"
##        secondLetter = entry2[1]
##        thirdLetter = entry2[2]
       
        entry3 = entry2 + firstLetter + pyg
        entry3 = entry3[1:len(entry3)]
        print entry3
    else:
        print "Entry was empty or does not only include letters."    
       
except Exception, e:
    str(e)