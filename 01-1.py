with open('01-input.txt', 'r') as file:
    data = file.read()

left_column = []
right_column = []
for line in data.split('\n'):
    split = line.split('   ')
    left_column.append(int(split[0]))
    right_column.append(int(split[1]))

left_column.sort()
right_column.sort()

distance = 0
for i in range(len(left_column)):
    distance += abs(left_column[i] - right_column[i])

print(distance)