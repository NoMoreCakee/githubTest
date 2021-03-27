#Case switcher

text = str(input('Text: '))
changedtext = ''

for letters in text:
    if letters.isupper() == True:
        letters.lower()
        changedtext += letters

    else:
        letters.upper()
        changedtext += letters

print(changedtext)
print(letters)