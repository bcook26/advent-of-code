# Bryce Cook 
# 12/4/2022
# Day 1
"""


This example list uses single-digit section IDs to make it easier to draw; 
your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. 
For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully 
contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning,
 so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.
"""

with open('input4.txt', 'r', encoding = 'UTF-8') as f: 
    f = f.read().strip()
    pairList = [x.strip() for x in f.split('\n')]
    print(pairList)

pairs1 = 0
pairs2 = 0

for line in pairList: 
    first, second = line.split(',')
    start1, end1 = first.split('-')
    start2, end2 = second.split('-')
    start1, end1, start2, end2 = [int(x) for x in [start1,end1,start2,end2]]
    print(start1, end1, start2, end2)

    # if (start2,end2) is full union of (start1,end1) (p1)
    if (start1 <= start2) and (end2 <= end1) or (start2 <= start1) and (end1 <= end2):
        pairs1 += 1
    
    # if (start2, end2) overlaps (start1, end1) not completely to the left or right (p2)

    if not (end1 < start2 or start1 > end2):
        pairs2 += 1

print(pairs1) # -> 571
print(pairs2) # -> 917

