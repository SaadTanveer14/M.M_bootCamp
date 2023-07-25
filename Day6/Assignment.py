sampleText = """Lorem ipsum dolor sit amet consectetur adipiscing elit Sed at magna libero
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas Proin
dictum odio eget consectetur lacinia mi dui semper odio in posuere tellus elit eget enim Donec lacinia
orci id purus fringilla fringilla Nullam in sapien quis ex facilisis euismod Nunc condimentum lacinia nisl sit
amet vestibulum libero convallis ac Nam bibendum tellus at massa elementum varius Vivamus
consequat elit nec vestibulum iaculis velit urna mattis arcu nec rutrum orci turpis vel urna Ut tempor
nunc at orci facilisis fringilla Nulla facilisi Duis sagittis odio et pharetra rhoncus nulla justo tincidunt
mauris nec porttitor tortor justo non orci In hac habitasse platea dictumst"""


# Punctuation and Special Characters Missing period so that we can seperate sentences
punc = "''!()-[]{};:'\"\\,<>/?@#$%^&*_~''"

cleanedText = ""


# Removing special characters and puctuation marks
for char in sampleText:
    if char not in punc:
        cleanedText+=char

longestWord = ""

# Spliting on the Basis of "." to get all the sentences
newText = cleanedText.split(".")


# Adding full Stop
firstSentence = newText[0]+"."

# Adding full Stop
secondSentence = newText[-2]+"."

# Removing left space
secondSentence = secondSentence.lstrip()


spaceCount = 0
uniqueChar = ""
cleanedTextFinal = ""


#  Removing periods from the final sentences so that fullstop is not counted in word length
#  Counting Spaces
#  Getting unique characters other than special characters.
for char in cleanedText:
    if char != ".":
        cleanedTextFinal+=char

    if char ==" ":
        spaceCount+=1
    elif char != "\n" and char.lower() not in uniqueChar and char != ".":
        uniqueChar+=char.lower()  


# Spliting the words on the basis of Spaces
words = cleanedTextFinal.split()

# Finding Longest Word
for word in words: 
    if len(word) > len(longestWord):
        longestWord = word




# Printing First Sentence
print("First Sentence:",'"' + firstSentence + '"')

# Printing Last Sentence
print("Last Sentence:",'"' + secondSentence + '"')

# Printing Longest Word
print("Longest Word: \"", longestWord+"\"", "(Length:"+str(len(longestWord))+")")

# Printing Space Count
print("Space Count: ", spaceCount)

# Counting Unique Characters and printing them
print("Unique Characters: ")
for char in uniqueChar: 
    print(char," ",str(cleanedText.count(char)))

# printing Cleaned Text
print("Cleaned Text:", cleanedTextFinal)
