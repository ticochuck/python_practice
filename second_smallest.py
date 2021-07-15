# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

import sys

data = []
for _ in range(int(input('How many cases: \n'))):
    name = input('Name: \n')
    score = int(input('Grade: \n'))
    data.append([name, score])

smallest = sys.maxsize
second = sys.maxsize

for entry in data:
    if entry[1] < smallest:
        second = smallest
        smallest = entry[1]
        
    elif entry[1] < second and entry[1] > smallest:
        second = entry[1]

for name in data:
    if name[1] == second:
        print(name[0])
