with open('01-input.txt', 'r') as file:
    data = file.read()

left_column = []
right_column = []
for line in data.split('\n'):
    split = line.split('   ')
    left_column.append(int(split[0]))
    right_column.append(int(split[1]))

similarity_score = 0
similarity_map = dict()
for i in range(len(left_column)):
    left_number = left_column[i]
    if left_number in similarity_map:
        similarity_score += similarity_map[left_number]
    else:
        occurences = 0
        for j in range(len(right_column)):
            right_number = right_column[j]
            if left_number == right_number:
                occurences += 1
        similarity_map[left_number] = left_number * occurences
        similarity_score += left_number * occurences

print(similarity_score)