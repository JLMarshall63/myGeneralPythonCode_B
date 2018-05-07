fName = r'C:\EsriPress\Python\Data\Exercise07\Results\textTest.txt'
myFile = open(fName, "r")

lines = myFile.readlines()

for line in lines:
##    print line
##    print line.rstrip()
    print line.rstrip().upper()

myFile.close()

##myFile = open(fName, "w")
##addCats = ["Smokey", "Sam", "Sabrina", "Alley Cat", "Tom Cat"]
##for cat in addCats:
   # myFile.write(cat + "\n")