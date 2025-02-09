# 1. Check for Duplicates
def contains_duplicates(arr):
    return len(arr) != len(set(arr))

arr1 = [1, 2, 4, 2, 5, 9]
print(contains_duplicates(arr1))  # Output: True

# 2. Rotate Array by k Steps
def rotate_array(arr, k):
    k = k % len(arr)  # To handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]

arr2 = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(arr2, 3))  # Output: [5, 6, 7, 1, 2, 3, 4]

# 3. Reverse Array In-Place
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr3 = [2, 4, 5, 7, 9, 12]
print(reverse_in_place(arr3))  # Output: [12, 9, 7, 5, 4, 2]

# 4. Find Maximum Element
def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

arr4 = [10, 5, 20, 8, 15]
print(find_max(arr4))  # Output: 20

# 5. Remove Duplicates from Sorted Array
def remove_duplicates(arr):
    if not arr:
        return []
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    return arr[:unique_index + 1]

arr5 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr5))  # Output: [1, 2, 3, 4, 5]

