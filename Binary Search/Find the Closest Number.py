# Given a sorted array and a target number.
# Our goal is to find a number in the array that is closest to the target number.
# We will be making use of a binary search to solve this problem

def find_closest_num(A, target):
    min_diff = min_diff_right = min_diff_left = float('inf')
    start = 0
    end = len(A) - 1
    closest_num = None

    # Check Edge case if data set contain None or 1 element
    if not A:
        return None
    if len(A) == 1:
        return A[0]

    while start <= end:
        mid = (start + end) // 2

        # Check you are not reading beyond the bounds of data set
        if mid+1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)

        # Check if the absolute difference value b/w left and right elements
        # are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Move the mid point
        if A[mid] < target:
            end = mid - 1
        elif A[mid] > target:
            end = mid + 1
            if end < 0:
                return A[mid]
        # If the element itself is the target, the closest
        # num to it is itself.
        else:
            return A[mid]

    return closest_num
