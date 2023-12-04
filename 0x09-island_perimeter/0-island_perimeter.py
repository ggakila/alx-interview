#!/usr/bin/python3
"""module to find island perimeter"""


def island_perimeter(grid):
    # Initialize perimeter
    perimeter = 0

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is land
            if grid[i][j] == 1:
                # Add 4 to the perimeter
                perimeter += 4

                # If the cell to the left is land, subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # If the cell above is land, subtract 2 from the perimeter
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter