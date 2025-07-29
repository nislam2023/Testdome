#https://www.testdome.com/questions/python/two-sum/94858

def find_two_sum(numbers, target_sum):
    matching_pairs=[]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            current_sum = numbers[j]+numbers[i]
            if current_sum == target_sum:
                print(numbers[i], numbers[j], current_sum)
                matching_pairs.append((numbers[i], numbers[j]))
                return i, j
    if matching_pairs:
        print("Matching pairs that sum to target value:")
        print(matching_pairs)
    else:
        print("❌ No matching pairs found.")
        return None
if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))




# numbers=[3, 1, 5, 7, 5, 9]
# target_sum=10
# matching_pairs=[]
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         current_sum = numbers[j]+numbers[i]
#         if current_sum == target_sum:
#             print(numbers[i], numbers[j], current_sum)
#             matching_pairs.append((numbers[i], numbers[j]))
#             # return i, j
# if matching_pairs:
#     print("Matching pairs that sum to target value:")
#     print(matching_pairs)
# else:
#     print("❌ No matching pairs found.")