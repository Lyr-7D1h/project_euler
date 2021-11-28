def build_grid(size):
    grid = []

    for y in range(size + 1):
        grid.append([])
        for x in range(size + 1):
            if y == size:
                grid[y].append([False, True])
            elif x == size:
                grid[y].append([True, False])
            else:
                grid[y].append([True, True])

    return grid


def has_path(grid, y, x):
    grid_size = len(grid) - 1

    # Is at the end?
    if x == grid_size and y == grid_size:
        return True

    # Go right if possible
    if grid[y][x][1]:
        grid[y][x][1] = False
        return has_path(grid, y, x + 1)

    # Go down if possible
    if grid[y][x][0]:
        grid[y][x][0] = False
        return has_path(grid, y + 1, x)

    return False


def count_pathways(grid):
    c = 0
    while has_path(grid, 0, 0):
        c += 1
    return c


grid = build_grid(2)
print(count_pathways(grid))
for x in grid:
    print(x)
