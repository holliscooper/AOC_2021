# preprocess input
with open('input6.txt') as file:
    for line in file:
        numbers = [int(s) for s in line.split(',') if s.isdigit()]

current_list = numbers
new_list = []
cycles = 256

for i in range(cycles):

    new_list = []
    for num in current_list:
        if num > 0:
            new_num = num - 1
            new_list.append(new_num)
        elif num == 0:
            new_list.append(6)
            new_list.append(8)
    current_list = new_list

count = len(new_list)
print(count)