try:
    fileName = 'C:\University of Washington GIS\UOWSummer2017\GEOG565\TextDocs\myTestA.txt'
    with open(fileName) as file_object:
        contents = file_object.read()
    print(contents)

except Exception, e:
    str(e)