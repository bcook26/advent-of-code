testing = False

if testing:
    # Test path
    path = 'Day8/example_input.txt'
else:
    # True path
    path = 'Day8/input.txt'

# parse input
with open(path, 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

grid_height = len(grid)
grid_width = len(grid[0])
print(f"Size of the Grid: {grid_height} x {grid_width}")

def is_visible(grid: list[list], row: int, col: int) -> bool:
    """Check if the tree at (row, col) is visible from any edge."""
    height = grid[row][col]
    # Check left
    if all(grid[row][c] < height for c in range(0, col)):
        return True
    
    # Check right
    if all(grid[row][c] < height for c in range(col+1, grid_width)):
        return True
    
    # Check up
    if all(grid[r][col] < height for r in range(0, row)):
        return True
    
    # Check down
    if all(grid[r][col] < height for r in range(row+1, grid_height)):
        return True
    return False

# All edge trees are visible
edge_count = (grid_height * 2 + grid_width * 2 - 4) if grid_height > 1 \
    and grid_width > 1 else max(grid_height, grid_width)

# keep track of visible trees and each tree's scenic score
visible_interior = 0
max_scenic_score = 0

for row in range(1, grid_height-1):
    for col in range(1, grid_width-1):

        # Part 1: Visibility
        if is_visible(grid, row, col):
            visible_interior += 1

        # Part 2: Scenic score calculation
        current_cell = grid[row][col]
        
        # Up
        up = 0
        for r in range(row-1, -1, -1):
            up += 1
            if grid[r][col] >= current_cell:
                break

        # Down
        down = 0
        for r in range(row+1, grid_height):
            down += 1
            if grid[r][col] >= current_cell:
                break

        # Left
        left = 0
        for c in range(col-1, -1, -1):
            left += 1
            if grid[row][c] >= current_cell:
                break

        # Right
        right = 0
        for c in range(col+1, grid_width):
            right += 1
            if grid[row][c] >= current_cell:
                break

        scenic_score = up * down * left * right
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

# Consider both edge and interior trees
final_tree_count = edge_count + visible_interior

print("Visible Trees Count: ", final_tree_count)
print("Max Scenic Score: ",max_scenic_score)

""" main components
  - parse input
    - read each line of the file
    - split into a grid of integers
    - determine the size of the grid:

  - determine if there is enough tree cover to keep tree house 'hidden'
    - count number of trees visible outside the grid
      when looking directly along a row/column

  - each tree is represented by a single digit who's value is its height (0 shorted, 9 tallest)
  - visible trees are those that are taller than all the trees between it and the edge of the grid
   - only look up down left, right (no diagonals)
  - all edges are visible

"""