def set_mines(grid, mines):
    for mine in mines:
        grid[mine[0]][mine[1]] = 9
    return grid


def set_nums(grid, SIZE):
    for row in range(SIZE):
        # Add an empty array that will hold each cell
        # in this row
        for column in range(SIZE):
            if grid[row][column] == 9:
                if column - 1 >= 0:
                    if grid[row][column - 1] != 9:
                        grid[row][column - 1] += 1
                if column + 1 < SIZE:
                    if grid[row][column + 1] != 9:
                        grid[row][column + 1] += 1
                if row - 1 >= 0:
                    if grid[row - 1][column] != 9:
                        grid[row - 1][column] += 1
                    if column - 1 >= 0:
                        if grid[row - 1][column - 1] != 9:
                            grid[row - 1][column - 1] += 1
                    if column + 1 < SIZE:
                        if grid[row - 1][column + 1] != 9:
                            grid[row - 1][column + 1] += 1
                if row + 1 < SIZE:
                    if grid[row + 1][column] != 9:
                        grid[row + 1][column] += 1
                    if column - 1 >= 0:
                        if grid[row + 1][column - 1] != 9:
                            grid[row + 1][column - 1] += 1
                    if column + 1 < SIZE:
                        if grid[row + 1][column + 1] != 9:
                            grid[row + 1][column + 1] += 1
    return grid


def find_other_open(open_area, grid, SIZE):
    for square in open_area:
        if 0 <= square[0] + 1 < SIZE:
            if grid[square[0] + 1][square[1]] == 0 and not ([square[0] + 1, square[1]]) in open_area:
                open_area.append([square[0] + 1, square[1]])
        if 0 <= square[0] - 1 < SIZE:
            if grid[square[0] - 1][square[1]] == 0 and not ([square[0] - 1, square[1]]) in open_area:
                open_area.append([square[0] - 1, square[1]])
        if 0 <= square[1] - 1 < SIZE:
            if grid[square[0]][square[1] - 1] == 0 and not ([square[0], square[1] - 1]) in open_area:
                open_area.append([square[0], square[1] - 1])
            if 0 <= square[0] + 1 < SIZE:
                if grid[square[0] + 1][square[1] - 1] == 0 and not ([square[0] + 1, square[1] - 1]) in open_area:
                    open_area.append([square[0] + 1, square[1] - 1])
            if 0 <= square[0] - 1 < SIZE:
                if grid[square[0] - 1][square[1] - 1] == 0 and not ([square[0] - 1, square[1] - 1]) in open_area:
                    open_area.append([square[0] - 1, square[1] - 1])
        if 0 <= square[1] + 1 < SIZE:
            if grid[square[0]][square[1] + 1] == 0 and not ([square[0], square[1] + 1]) in open_area:
                open_area.append([square[0], square[1] + 1])
            if 0 <= square[0] + 1 < SIZE:
                if grid[square[0] + 1][square[1] + 1] == 0 and not ([square[0] + 1, square[1] + 1]) in open_area:
                    open_area.append([square[0] + 1, square[1] + 1])
            if 0 <= square[0] - 1 < SIZE:
                if grid[square[0] - 1][square[1] + 1] == 0 and not ([square[0] - 1, square[1] + 1]) in open_area:
                    open_area.append([square[0] - 1, square[1] + 1])
    return open_area


def is_in_open_areas(loc, open_areas):
    for areas in open_areas:
        if loc in areas:  # areas.contains(loc):
            return True
    return False


def zeros_not_in_area(grid, open_areas, SIZE):
    for row in range(SIZE):
        for column in range(SIZE):
            if grid[row][column] == 0 and not is_in_open_areas([row, column], open_areas):
                return True
    return False


def set_open_areas(grid, SIZE):
    open_areas = []
    while zeros_not_in_area(grid, open_areas, SIZE):
        open_area_0 = []
        open_areas.append(open_area_0)

        for row in range(SIZE):
            for column in range(SIZE):
                if grid[row][column] == 0 and not is_in_open_areas([row, column], open_areas):
                    open_area_0.append([row, column])
                    open_area_0 = find_other_open(open_area_0, grid, SIZE)

        temp = []

        for square in open_area_0:
            if 0 <= square[0] + 1 < SIZE:
                if grid[square[0] + 1][square[1]] != 9:
                    temp.append([square[0] + 1, square[1]])
            if 0 <= square[0] - 1 < SIZE:
                if grid[square[0] - 1][square[1]] != 9:
                    temp.append([square[0] - 1, square[1]])
            if 0 <= square[1] - 1 < SIZE:
                if grid[square[0]][square[1] - 1] != 9:
                    temp.append([square[0], square[1] - 1])
                if 0 <= square[0] + 1 < SIZE:
                    if grid[square[0] + 1][square[1] - 1] != 9:
                        temp.append([square[0] + 1, square[1] - 1])
                if 0 <= square[0] - 1 < SIZE:
                    if grid[square[0] - 1][square[1] - 1] != 9:
                        temp.append([square[0] - 1, square[1] - 1])
            if 0 <= square[1] + 1 < SIZE:
                if grid[square[0]][square[1] + 1] != 9:
                    temp.append([square[0], square[1] + 1])
                if 0 <= square[0] + 1 < SIZE:
                    if grid[square[0] + 1][square[1] + 1] != 9:
                        temp.append([square[0] + 1, square[1] + 1])
                if 0 <= square[0] - 1 < SIZE:
                    if grid[square[0] - 1][square[1] + 1] != 9:
                        temp.append([square[0] - 1, square[1] + 1])

        open_area_0.extend(temp)

    return open_areas
