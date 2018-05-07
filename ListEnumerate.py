import string
alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

print alphabet

for l in alphabet:
    print l

for l in enumerate(alphabet):
    print l    