try:
    entry = raw_input("Enter input here: ")
    #print entry

    if (entry[0] == "A" or entry[0] == "E" or entry[0] == "I" or entry[0] == "O"  or entry[0] == "U"):
        print entry + "way"

    else:
        x = entry[-1]
        y = entry[-2]
        z = y + x

        #print z
##    print(myString[4:6])
##    print(myString[4:6]) + myString + "ay"
        print z + entry + "ay"

except Exception, e:
    str(e)
    