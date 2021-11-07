# A fixed point in an array A is an index i such that A[i] is equal to i.


def fixed_point(A):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2
        if A[mid] == mid:
            return A[mid]
        elif A[mid] < mid:
            start = mid+1
        else:
            end = mid-1
    return "No fixed point"


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "No fixed point":
A3 = [-10, -5, 3, 4, 7, 9]

print(A1)
print(fixed_point(A1))
print(A2)
print(fixed_point(A2))
print(A3)
print(fixed_point(A3))
