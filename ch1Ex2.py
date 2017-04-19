#!/usr/bin/env python3

numbers = []
counter = 0

while True:
    try:
        num = input("enter a number or Enter to finish: ")
        if num == '':
            break
        numbers.append(int(num))
        counter += 1
    except ValueError as err:
        print(err)
        continue
summa = sum(numbers)
mean = summa / counter
minimum = min(numbers)
maximum = max(numbers)

print('[%s]' % ', '.join(map(str, numbers)))
print('count = %i sum = %i lowest = %i highest = %i mean = %i' % (counter, summa, minimum, maximum, mean))
