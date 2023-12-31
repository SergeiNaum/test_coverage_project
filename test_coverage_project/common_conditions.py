test_data_get = [
    [[1, 2, 3], 1],
    [[1, 2, 3, 5], 5, "val"],
    [[1, 2, 3, 4], 5],
    [[7, 8, 9], -4],
    [[7, 8, 9], 1],
    [[7, 8, 9], 0, "c"],
]


test_data_test_index = [
    [[1, 2, 3, 2, 5], 2],
    [[1, 2, 3, 2, 5], 7],
    [[], 1],
    [[1, 2, 3, 2, 5], 2, -3],
    [[1, 2, 3, 2, 5], 1, -6],
    [[1, 2, 3, 4, 5, 6], 4, 1],
]


test_data_test_slice = [
    [[1, 2, 3, 4, 5, 6], 1, 4],
    [[1, 2, 3, 4, 5]],
    [[1, 2, 3, 4, 5], -4, -2],
    [[1, 2, 3, 4, 5], 7],
    [[], 7],
    [[1, 2, 3, 2, 5], -4],
    [[1, 2, 3, 2, 5], -5],
    [[1, 2, 3, 4, 5, 6], -2, 4],
    [[1, 2, 3, 4, 5], -20],
]


conditions_get = [
    "[1, 2, 3], 1 == 2",
    "[1, 2, 3, 5], 5, val == val",
    "[1, 2, 3, 4], 5 == None",
    "[7, 8, 9], -4 == None",
    "[7, 8, 9], 1 ==  8",
    "[7, 8, 9], 0, c  == 7",
]


conditions_index = [
    "[1, 2, 3, 2, 5], 2) == 1",
    "[1, 2, 3, 2, 5], 7) == -1",
    "[], 1) == -1",
    "[1, 2, 3, 2, 5], 2, -3) == 3",
    "[1, 2, 3, 2, 5], 1, -6) == 0",
    "[1, 2, 3, 4, 5, 6], 4, 1) == 3",
]


conditions_slice = [
    "[1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]",
    "[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]",
    "[1, 2, 3, 4, 5], -4, -2) == [2, 3]",
    "[1, 2, 3, 4, 5], 7) == []",
    "[], 7) == []",
    "[1, 2, 3, 2, 5], -4) == [2, 3, 2, 5]",
    "[1, 2, 3, 2, 5], -5) == [1, 2, 3, 2, 5]",
    "[1, 2, 3, 4, 5, 6], -2, 4) == []",
    "[1, 2, 3, 4, 5], -20) == [1, 2, 3, 4, 5]",
]
