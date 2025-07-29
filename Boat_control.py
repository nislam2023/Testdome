import numpy as np

game_matrix = [
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],
    [False, True, True, False, True, True],
    [False, True, True, True, False, True],
    [False, False, False, False, False, False],
]

# Find indices where matrix1 is True
indices = np.argwhere(game_matrix)
# print("Indices where matrix1 is True:\n", indices)

from_row = 3
from_column = 2
to_row = 6
to_column = 2

index_check = np.array([(to_row, to_column)])
max_threshold = np.max(indices)
if index_check.all() < max_threshold:
    for i, j in indices:
        # print(i, j)
        # filtered_arr = np.where(index_check >= max_threshold, indices, 0)
        # if index_check.any() < max_threshold:
        #     print('cant move,Out of bounds')
        if i == to_row and j == to_column:
            # print(i,to_row, j,to_column)
            if from_row == to_row:
                if from_column + - 1 == to_column:
                    print("Valid move1")
                    # return True
                else:
                    print("can't move,can't travel through land")
                    # return False
        elif from_column == to_column:
            if from_row + - 1 == to_row:
                print("Valid move2")
                    # return False
                    # return True
else:
    print('cant move,Out of bounds')
    # return False




# Your 19x2 array
arr = np.random.randint(1, 100, size=(19, 2))  # example array

# Four variables
a, b, c, d = 50, 25, 80, 10

# Stack the variables into an array
vars_array = np.array([a, b, c, d])

# Check if each variable is greater than *any* element in arr
result = vars_array[:, None, None] > arr  # shape: (4, 19, 2)
any_greater = np.any(result, axis=(1, 2))  # shape: (4,)

print("Array:\n", arr)
print("Each variable > any element in array:\n", any_greater)
