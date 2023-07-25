
print("==================== Enter Your Marks to get your Grade ====================")

# Input from User
input_marks = float(input("Enter Marks in Number :- "))

# Invalid Inputs
if input_marks < 0 or input_marks > 100:
    print("Invalid Marks")

elif 0 <= input_marks < 60:
    print(":( You Failed with Grade 'F' ): ")

elif 60 <= input_marks < 70:
    print("You Passed with Grade 'D' ")

elif 70 <= input_marks < 80:
    print("You Passed with Grade 'C' ")

elif 80 <= input_marks < 90:
    print(":) Congratulation You Passed with Grade 'B' (:")

elif 90 <= input_marks <= 100:
    print(" `````~~~~~~~~~ Excellent performance You Passed with Grade 'A'  ~~~~~~~~~``````")
