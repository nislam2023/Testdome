import numpy as np

game_matrix = np.array([
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],
    [False, True, True, False, True, True],
    [False, True, True, True, False, True],
    [False, False, False, False, False, False],
])

# Find indices where matrix1 is True
indices = np.argwhere(game_matrix)
land_indices = np.argwhere(~game_matrix)
from_row = 2
from_column = 2
to_row = 2
to_column = 4

from_row = 3
from_column = 2
to_row = 3
to_column = 4
index_check = np.array([to_row, to_column])
max_threshold = np.max(indices)
if np.all(index_check <= max_threshold):
    for i, j in indices:
        if i == to_row and j == to_column:
            # print(i,to_row, j,to_column)
            if from_row == to_row:
                # if np.any(np.all(indices == (to_row,to_column),axis=1)):
                stat_pos = [from_row, from_column]
                target_pair = [to_row, to_column]
                indices_found = np.where((indices[:, 0] == target_pair[0]) & (indices[:, 1] == target_pair[1]))
                land_indices_found = np.where(
                    (land_indices[:, 0] == target_pair[0]) & (land_indices[:, 1] == target_pair[1]))
                print("Valid move1")
                # return True
                if np.all(indices[from_column] == indices[to_column]):
                    print("Valid move2")
                elif np.any(land_indices[from_column] == indices[to_column]):
                    print("can't move,can't travel through land")
                    # return False
            elif from_column == to_column:
                if np.any(np.all(land_indices != (to_row, to_column), axis=1)):
                    print("Valid move3")
        # else:
        #     print('Land, cant move')

else:
    print('cant move,Out of bounds')
    # return False

ddd = np.where(indices[:, 0] == target_pair[0])
for inc in ddd:
    lst = indices[inc][:, 1]
    lst2 = [l for l in range(lst[0],max(lst),1)]
    if np.all(lst==lst2):
        print("Proced")
    else:
        print("No common elements found.")
