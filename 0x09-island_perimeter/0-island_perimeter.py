#!/usr/bin/python3
"""module to find island perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # up
                if i - 1 < 0:
                    count += 1
                else:
                    try:
                        if grid[i - 1][j] == 0 or i - 1 < 0:
                            count += 1
                    except:
                        pass
                # down
                if i + 1 > len(grid) - 1:
                    count += 1
                else:
                    try:
                        if grid[i + 1][j] == 0:
                            count += 1
                    except:
                        pass
                # check right
                if j + 1 > len(grid[i]) - 1:
                    count += 1
                else:
                    try:
                        if grid[i][j + 1] == 0:
                            count += 1
                    except:
                        pass
                # check left
                try:
                    if grid[i][j - 1] == 0 or j - 1 < 0:
                        count += 1
                except:
                    pass
    return count