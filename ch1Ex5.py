#!/usr/bin/env python3

numbers = []

while True:
    try:
        num = input("enter a number or Enter to finish: ")
        if num == '':
            break
        numbers.append(int(num))
    except ValueError as err:
        print(err)
        continue
counter = len(numbers)
summa = sum(numbers)
mean = summa / counter
minimum = min(numbers)
maximum = max(numbers)

i, j = 0, 0
while i < counter-1:
    while j < counter-1:
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        j += 1
    i += 1

c = str(counter / 2)
if c[len(c)-1] == '0':
    mediana = numbers[int(counter/2)] + numbers[int(counter/2)-1] / 2
else:
    mediana = numbers[int(counter/2)]

print('[%s]' % ', '.join(map(str, numbers)))
print('count = %i sum = %i lowest = %i highest = %i mean = %f median = %f' % (counter, summa, minimum, maximum, mean, mediana))
