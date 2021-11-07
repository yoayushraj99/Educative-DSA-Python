# determines the index of the smallest element of the cyclically shifted array.
# An array is “cyclically shifted” if it is possible to shift its entries cyclically so that it becomes sorted.

def find_lowest_num_index(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
            return A[mid+1]
        elif A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
            return A[mid]
        elif A[low] < A[high] or A[low] > A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(find_lowest_num_index([7,1,2,3,4,5,6]))
