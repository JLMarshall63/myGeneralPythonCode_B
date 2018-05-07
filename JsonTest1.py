import json
data = json.load(open("C:\\University of Washington GIS\UOWSummer2017\\GEOG565\\PythonScripts\\GenPython_Scripts\\jsondictionary\\dictionary-master\\dictionary.json"))

def translate(w):
    return data(w)

word = str(input("Enter word."))

print(translate(word))