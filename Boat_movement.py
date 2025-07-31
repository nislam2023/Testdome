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

"""simple valid move"""
from_row = 3
from_column = 2
to_row = 2
to_column = 2

"""out of bound"""
from_row = 0
from_column = 0
to_row = 5
to_column = 3

"""same row, column moves 2 step in water"""
from_row = 2
from_column = 2
to_row = 2
to_column = 4

"""same row, column has land"""
from_row = 3
from_column = 2
to_row = 3
to_column = 4

"""same column, next valid row move"""
from_row = 3
from_column = 2
to_row = 4
to_column = 2

index_check = np.array([to_row, to_column]).flatten()
# max_threshold = np.max(indices)
target_pair = [to_row, to_column]
start_pair = [from_row, from_column]

# Step 2: Check if any row in arr_19x2 matches this
# exists = np.any(np.all(arr_19x2 == needle_flat, axis=1))
# if np.all(index_check <= max_threshold):
if np.any(np.all(index_check == indices, axis=1)):
    for i, j in indices:
        if i == to_row and j == to_column:
            if from_row == to_row:

                # find same row same but column different
                indices_found = np.where((indices[:, 0] == target_pair[0]))

                same_row_indices = [indices[indices_found[0][i]].tolist()
                                    for i in range(len(indices_found[0]))]
                land_indices_found = np.where(land_indices[:, 0] == target_pair[0])

                same_row_land_indices = [land_indices[land_indices_found[0][i]].tolist()
                                         for i in range(len(land_indices_found[0]))]

                start_value = start_pair[1]
                if start_pair[0] < target_pair[0]:
                    step = -1  # Change to -1 to step backward
                else:
                    step = 1

                # Convert to sets for fast lookup
                set1 = set(tuple(x) for x in same_row_indices)
                set2 = set(tuple(x) for x in same_row_land_indices)

                # Calculate new_pair by stepping from start_pair
                current = start_pair[1] + step
                new_pair = (start_pair[0], current)

                target_tuple = tuple(target_pair)

                # First, check if target is blocked
                if target_tuple in set2:
                    print(f"❌ Invalid move: target {target_tuple} is in a land area")
                else:
                    current = start_pair[1]
                    row = start_pair[0]

                    while True:
                        current += step
                        current_pair = (row, current)

                        if current_pair == target_tuple and current_pair in set1:
                            print(f"✅ Valid move: reached target {current_pair} ")
                            break
                        elif current_pair not in set1:
                            print(f"⚠️ Invalid path: {current_pair} can not move through land")
                            break

            elif from_column == to_column:

                indices_found = np.where((indices[:, 1] == target_pair[1]))  # find same column same but
                # row different

                same_column_indices = [indices[indices_found[0][i]].tolist()
                                       for i in range(len(indices_found[0]))]
                land_indices_found = np.where(land_indices[:, 1] == target_pair[1])

                same_column_land_indices = [land_indices[land_indices_found[0][i]].tolist() for i in
                                            range(len(land_indices_found[0]))]

                # Start from a specific pair in list1
                start_value = start_pair[0]

                if start_pair[0] > target_pair[0]:
                    step = -1  # Change to -1 to step backward
                else:
                    step = 1

                # Convert to sets for fast lookup
                set1 = set(tuple(x) for x in same_column_indices)
                set2 = set(tuple(x) for x in same_column_land_indices)

                # Calculate new_pair by stepping from start_pair
                current = start_pair[0] + step
                new_pair = (current, start_pair[1])

                target_tuple = tuple(target_pair)

                # First, check if target is blocked
                if target_tuple in set2:
                    print(f"❌ Invalid move: target {target_tuple} is in a blocked area (list2)")
                else:
                    current = start_pair[0]
                    column = start_pair[1]

                    while True:
                        current += step
                        current_pair = (current, column)

                        if current_pair == target_tuple and current_pair in set1:
                            print(f"✅ Valid move: reached target {current_pair} ")
                            break
                        elif current_pair not in set1:
                            print(f"⚠️ Invalid path: {current_pair} can not move through land")
                            break
else:
    print('cant move,Out of bounds')
    # return False
