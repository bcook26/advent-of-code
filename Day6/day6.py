# Bryce Cook 
# 12/6/2022
# Day 6

with open('input6.txt','r') as f: 
    input = f.read()

def DetectTarget(input: str, size: int):
    sz = len(input)

    for i in range(sz - size + 1):
        s = set(input[i:i + size])

        if len(s) == size:
            return i + size

    return print("No markers")

# solutions 
print('Answer for part 1 is: ', str(DetectTarget(input, 4)))

print('Answer for part 2 is: ', str(DetectTarget(input, 14)))




