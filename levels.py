def get_level_things(level):
    if level == 1:
        SIZE = 8
        mines = [[0, 0], [1, 0], [0, 4], [1, 4], [2, 4], [2, 5], [3, 5], [7, 2], [7, 3], [7, 4]]
        return [SIZE, mines]

    if level == 2:
        SIZE = 9
        mines = [[0, 8], [1, 4], [2, 6], [5, 0], [5, 6], [6, 4], [6, 6], [7, 7], [8, 8]]
        return [SIZE, mines]

    if level == 3:
        SIZE = 9
        mines = [[0, 0], [0, 4], [3, 1], [3, 2], [3, 3], [5, 8], [6, 8], [7, 6], [7, 8], [8, 4]]
        return [SIZE, mines]