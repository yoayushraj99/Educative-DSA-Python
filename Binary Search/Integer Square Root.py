# Your task is to return the largest integer
# whose square is less than or equal to the k from the function integer_square_root(k)
# given in the code widget below. The input parameter k is a non-negative integer.


def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        sqre_mid = mid ** 2

        if sqre_mid <= k:
            low = mid+1
        else:
            high = mid - 1
    return low - 1


print(integer_square_root(296))
