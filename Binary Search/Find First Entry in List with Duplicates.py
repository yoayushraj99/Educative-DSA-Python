# Write a function that takes an array of sorted integers and
# a key and returns the index of the first occurrence of that key from the array.


def find_first_duplicate(A, target):
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start + end) // 2

        if target < A[mid]:
            end = mid-1
        elif target > A[mid]:
            start = mid+1
        else:
            if target == A[mid-1]:
                end = mid-1
            else:
                return mid

    return None


A = [-14, -14, 2, 108, 243, 285, 285, 285, 401]
target = 2
x = find_first_duplicate(A, target)
print(x)
