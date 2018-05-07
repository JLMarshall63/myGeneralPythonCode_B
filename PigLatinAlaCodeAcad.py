try:
    entry = ""    
    entry = raw_input("Enter an English word here: ")
    if len(entry) > 0 and entry.isalpha():
        print entry
        xvar = entry[0]
        xentry = entry[1:]
        #print xentry
        print xentry + xvar.lower() + "ay"
    else:
        print "Entry was empty or does not only include letters."    
       
except Exception, e:
    str(e)