# using defaultdict to handle directories and their associated file sizes
from collections import defaultdict

directory_sums = defaultdict(int)
current_dir_stack = ['/']

testing = False

TOTAL_DISK_SPACE = 70_000_000
SPACE_REQUIRED = 30_000_000

if testing:
    # Test path
    path = 'Day7/example_input.txt'
else:
    # True path
    path = 'Day7/input.txt'

for line in open(path):
    cleaned_line = line.strip()

    # Handle commands
    if cleaned_line.startswith('$'):
        # if we're going up a directory
        if cleaned_line.startswith('$ cd ..'):
            # print("Back tracking a single directory")
            if len(current_dir_stack) > 1:
                current_dir_stack.pop()
        elif cleaned_line.startswith('$ cd /'):
            current_dir_stack = ['/']
        elif cleaned_line.startswith('$ cd '):
            # Going down a directory level
            dir_name = cleaned_line.split(' ')[-1]
            if current_dir_stack[-1] == '/':
                new_path = '/' + dir_name
            else:
                new_path = current_dir_stack[-1] + '/' + dir_name
            current_dir_stack.append(new_path)
    elif cleaned_line.startswith('dir'):
        # Found directory, do nothing
        pass
    else:
        # Handle file size computation
        file_size = int(cleaned_line.split(' ')[0])
        # Add the file size to all parent directories (including current)
        for path in current_dir_stack:
            directory_sums[path] += file_size
        
# Initialize start sum
total_sum = 0

# Part 1
for path, total in directory_sums.items():

    # print(f"Path: {path}, Total: {total}")
    if total <= 100000:
        total_sum += total

# Part 2
delete_options = {}
total_space_used = directory_sums['/']
unused_space = TOTAL_DISK_SPACE - total_space_used


for path, total in directory_sums.items():
    if SPACE_REQUIRED < unused_space + total <= TOTAL_DISK_SPACE:
        delete_options[path] = total

# Space required is the lower bound for installation
# if this is smaller than the size of unused space plus the size of the directory
# we can delete, then we can safely delete it with disk space left over

# Print solutions        
print(f"Part 1 solution: {total_sum}")
print(f"Part 2 solution: {min(delete_options.values())}")