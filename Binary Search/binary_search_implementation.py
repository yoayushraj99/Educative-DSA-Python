# Binary search assumes that the array on which the search will take place is sorted in ascending order.
# In binary search, the target element is compared with the middle element of the array following which the next chunk of the array to be searched is decided.
# If the target matches the middle element, we are successful.
# Otherwise, since the array is sorted, if the target is smaller than the middle element, it could only be in the left half of the array.
# Alternatively, if the target is greater than the middle element, it could be in the right half of the array.
# So, we exclude one half of the array from the further search and repeat the same strategy to the remaining half.


# Iterative Binary Search
def binary_search_iterative(data, target):
    if not data:
        return False
    end = len(data)-1
    start = 0

    while start<=end:
        mid = (start+end)//2
        if data[mid] == target:
            return True
        elif target <= data[mid]:
            end = mid-1
        else:
            start = mid+1
    return False


# Recursive Binary Search
def binary_search_recursive(data, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if target == data[mid]:
            return True
        elif target <= data[mid]:
            return binary_search_iterative(data, target, start, mid-1)
        else:
            return binary_search_iterative(data, target, mid+1, end)
