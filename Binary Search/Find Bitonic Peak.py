# given an array that is bitonically sorted,
# an array that starts off with increasing terms and then concludes with decreasing terms.
# In any such sequence, there is a “peak” element which is the largest element in the sequence.

# A bitonic sequence is a sequence of integers such that: x_0 < ... < x_k > ... > x_{n-1} for some k, 0 <=k < n

def find_bitonic_peak(A):
    start = 0
    end = len(A) - 1

    # Edge Case
    if len(A) < 3:
        return None

    while start <= end:
        mid = (start + end) // 2
        mid_left = A[mid-1] if mid-1 >= 0 else float('-inf')
        mid_right = A[mid+1] if mid+1 < len(A) else float('inf')

        if mid_left < A[mid] and mid_right > A[mid]:
            start = mid+1
        elif mid_left > A[mid] and mid_right < A[mid]:
            end = mid-1
        elif A[mid] > A[mid+1] and A[mid] > A[mid-1]:
            return A[mid]
    return None

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
