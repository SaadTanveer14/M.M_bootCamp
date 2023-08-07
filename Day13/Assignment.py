word = "error"

with open('test.txt', 'r') as file:
    data = file.readlines()

    for line in data:
        words = line.split()
        # print(words)
        if word in words:
            print(word)

table = 6
with open('table.txt', 'w') as file:
    for i in range(1, 11):
        file.write(str(table) + " x " + str(i) + " = " + str(table * i))
        file.write('\n')
