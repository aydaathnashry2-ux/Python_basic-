# Binary Search Algorithm
# Implemented by Ayda

def binary_search(arr, target):
    first_index = 0
    last_index = len(arr) - 1
    
    while first_index <= last_index:
        mid = (first_index + last_index) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first_index = mid + 1
        else:
            last_index = mid - 1
            
    return -1

my_arr = [1, 5, 7, 10]
target = 7
result = binary_search(my_arr, target)
print(result)
