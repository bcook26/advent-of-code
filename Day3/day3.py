# Bryce Cook 
# 12/3/2022
# Day 3

# --- Day 3: Rucksack Reorganization ---
"""
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

"""
# part 1
with open("input3.txt", "r") as rucksack:
    input = rucksack.read().strip()
    rucksack = input.split('\n')
    print(rucksack)
total = 0
for items in rucksack:
    firstpart, secondpart = set(items[:len(items)//2]), set(items[len(items)//2:])
    for char in firstpart: 
        if char in secondpart:
            value = ord(char) - 96 if char.islower() else ord(char) - 64 + 26
            total += value
            break

print(total)
# 7795

#part 2 using string method
import string

def get_priorities():
        lowercase = list(zip(list(string.ascii_lowercase), range(1, 27)))
        uppercase = list(zip(list(string.ascii_uppercase), range(27, 53)))

        return {i[0]: i[1] for i in lowercase + uppercase}

priorities = get_priorities()
total = 0
for i in range(0, len(rucksack), 3):
    a, b, c = set(rucksack[i]), set(rucksack[i + 1]), set(rucksack[i + 2])
    intersection = list(a.intersection(b).intersection(c))
    total += sum(priorities[i] for i in intersection)
    print(total)

# 2703

            

