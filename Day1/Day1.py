# Bryce Cook 
# 12/1/2022
# Day 1
# input is the number of calories an elf is carrying on hand

with open('Day1/input.txt', 'r') as f:
    rucksack = [x for x in f.read().strip().split('\n')]

largest = 0
second_largest = 0
third_largest = 0
count = 0 


for item in rucksack: 
    if item == '':
        count = 0
    else: 
        value = int(item)
        count += value

    if count > largest:
        third_largest = second_largest
        second_largest = largest
        largest = count
    elif count > second_largest:
        third_largest = second_largest
        second_largest = count
    elif count > third_largest: 
        third_largest = count

sum_of_largest = largest + second_largest + third_largest

print(f"answer to part 1: {largest}")
print(f"answer to part 2: {sum_of_largest}")
    
