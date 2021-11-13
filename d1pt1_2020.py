#Find two numbers in data file whose sum is 2020 and multiply them

numbers_weve_seen = set()

with open('data/day01.txt', 'r') as infile:
    for current_line in infile.readlines():
        current_number = int(current_line.strip())
        numbers_weve_seen.add(current_number)

for x in numbers_weve_seen:

    # subtract current number in 2020
    y = 2020 - x

    if y in numbers_weve_seen:
         product = y * x
         print(product)
         break