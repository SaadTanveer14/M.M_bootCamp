number_list = [1, 2, 4, 6, 0]
new_number_list = []
if len(number_list) < 2:
    new_number_list = number_list
else:  # Adding two Number and putting those two numbers on the left and right of sum
    i = 0
    while i < len(number_list):
        if i-1 < 0:
            new_number_list.append(number_list[i+1])
        elif i+1 > len(number_list)-1:
            new_number_list.append(number_list[i-1])
        else:
            new_number_list.append(number_list[i+1] + number_list[i-1])

        i += 1

print(new_number_list)
