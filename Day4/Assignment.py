


print("/////================================ Enter Your Marks to get your Grade ==========================================//////\n\n")

print("Marks :- ")

# Input from User
inputMarks = int(input())

# Invalid Inputs
if inputMarks < 0 and inputMarks >100:
    print("Invalid Marks")

elif inputMarks >= 0 and inputMarks < 60:
    print(":( You Failed with Grade 'F' ): ")

elif inputMarks >= 60 and inputMarks < 70:
    print("You Passed with Grade 'D' ")

elif inputMarks >= 70 and inputMarks < 80:
    print("You Passed with Grade 'C' ")

elif inputMarks >= 80 and inputMarks < 90:
    print(":) Congratulation You Passed with Grade 'B' (:")

elif inputMarks >= 90 and inputMarks <= 100:
    print(" `````~~~~~~~~~~~~~ Excellent performance You Passed with Grade 'A'  ~~~~~~~~~~~~~~~~``````")
