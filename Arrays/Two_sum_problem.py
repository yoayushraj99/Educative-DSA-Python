# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_method(arr, target):
    hash = dict()

    for i in range(len(arr)):
        if arr[i] in hash:
            return True
        else:
            hash[target-arr[i]] = arr[i]
    return False


print(two_sum_hash_method([-2, 1, 2, 4, 7, 11], 6))

# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum_binary_search_method(arr, target):
    i = 0
    j = len(arr)-1

    while i<j:
        if arr[i] + arr[j] == target:
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(two_sum_binary_search_method([-2, 1, 2, 4, 7, 11], 6))
