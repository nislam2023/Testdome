def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    import numpy as np

    game_matrix = np.array([
        [False, True, True, False, False, False],
        [True, True, True, False, False, False],
        [True, True, True, True, True, True],
        [False, True, True, False, True, True],
        [False, True, True, True, False, True],
        [False, False, False, False, False, False], ])

    indices = np.argwhere(game_matrix)
    land_indices = np.argwhere(~game_matrix)
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
                        return False
                    else:
                        current = start_pair[1]
                        row = start_pair[0]

                        while True:
                            current += step
                            current_pair = (row, current)

                            if current_pair == target_tuple and current_pair in set1:
                                print(f"✅ Valid move: reached target {current_pair} ")
                                return True
                                break
                            elif current_pair not in set1:
                                print(f"⚠️ Invalid path: {current_pair} can not move through land")
                                return False
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
                        print(f"❌ Invalid move: target {target_tuple} is in land")
                        return False
                    else:
                        current = start_pair[0]
                        column = start_pair[1]

                        while True:
                            current += step
                            current_pair = (current, column)

                            if current_pair == target_tuple and current_pair in set1:
                                print(f"✅ Valid move: reached target {current_pair} ")
                                return True
                                break

                            elif current_pair not in set1:
                                print(f"⚠️ Invalid path: {current_pair} can not move through land")
                                return False
                                break
    else:
        print('cant move,Out of bounds')
        return False


if __name__ == "__main__":
    game_matrix = [
        [False, True, True, False, False, False],
        [True, True, True, False, False, False],
        [True, True, True, True, True, True],
        [False, True, True, False, True, True],
        [False, True, True, True, False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(game_matrix, 3, 2, 2, 2))  # True, Valid move
    print(can_travel_to(game_matrix, 3, 2, 3, 4))  # False, Can't travel through land
    print(can_travel_to(game_matrix, 3, 2, 6, 2))  # False, Out of bounds
    print(can_travel_to(game_matrix, 2, 4, 6, 6))  # False, some coordinates out of grid
    print(can_travel_to(game_matrix, 2, 2, 2, 4))  # True, 2 steps of water
    print(can_travel_to(game_matrix, 2, 2, 2, 1))  # True, backward column move
    print(can_travel_to(game_matrix, 2, 2, 4, 2))  # True, same column
    print(can_travel_to(game_matrix, 0, 0, 5, 3))  # False, all coordinates inside grid
