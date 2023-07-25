sample_text = """saad tanveer"""


# Punctuation and Special Characters Missing period so that we can seperate sentences
punc = "''!()-[]{};:'\"\\,<>/?@#$%^&*_~''"

cleaned_text = ""

if sample_text[-1] != '.':
    sample_text+='.'



# Removing special characters and puctuation marks
for char in sample_text:
    if char not in punc:
        cleaned_text+=char

longest_word = ""

# Spliting on the Basis of "." to get all the sentences
new_text = cleaned_text.split(".")


# Adding full Stop
first_sentence = new_text[0]+"."

# Adding full Stop
second_sentence = new_text[-2]+"."

# Removing left space
second_sentence = second_sentence.lstrip()


space_count = 0
unique_char = ""
cleaned_text_final = ""


#  Removing periods from the final sentences so that fullstop is not counted in word length
#  Counting Spaces
#  Getting unique characters other than special characters.
for char in cleaned_text:
    if char != ".":
        cleaned_text_final+=char

    if char ==" ":
        space_count+=1
    elif char != "\n" and char.lower() not in unique_char and char != ".":
        unique_char+=char.lower()  


# Spliting the words on the basis of Spaces
words = cleaned_text_final.split()

# Finding Longest Word
for word in words: 
    if len(word) > len(longest_word):
        longestWord = word




# Printing First Sentence
print("First Sentence:",'"' + first_sentence + '"')

# Printing Last Sentence
print("Last Sentence:",'"' + second_sentence + '"')

# Printing Longest Word
print("Longest Word: \"", longestWord+"\"", "(Length:"+str(len(longest_word))+")")

# Printing Space Count
print("Space Count: ", space_count)

# Counting Unique Characters and printing them
print("Unique Characters: ")
for char in unique_char: 
    print(char," ",str(cleaned_text.count(char)))

# printing Cleaned Text
print("Cleaned Text:", cleaned_text_final)
