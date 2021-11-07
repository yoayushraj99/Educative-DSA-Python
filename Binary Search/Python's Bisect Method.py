# Bisect is a built - in binary search method in Python.
# It can be used to search for an element in a sorted list.

from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# The bisect_left function finds the index of the target element.
# In the event where duplicate entries are satisfying the target element, the bisect_left function returns the left-most occurrence.
# The input parameters to the method are the sorted list and the target element to be searched.


# First occurrence of 108 is at index 3
print(bisect_left(A, 108))


# The bisect_right function returns the insertion point which comes after,
# or to the right of, any existing entries of the target element in the list.
# It takes in a sorted list as the first parameter and the target element to be searched as the second parameter.

# Index position after last occurrence of 285 is 9.
print(bisect_right(A, 285))


# There is also just a regular default bisect function.
# This function is equivalent to bisect_right and
# takes a sorted list and the target element to be searched as input parameters.

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect(A, 285))


# Given that the list A is sorted, it is possible to insert elements into A so that the list remains sorted.
# Functions insort_left and insort_right behave in a similar way to bisect_left and bisect_right,
# only the insort functions insert at the index positions.
# The input parameters to the method are the sorted list and the element to be inserted at a position so that the list remains sorted.

print(A)
insort_left(A, 1)
print(A)

insort_right(A, 243)
print(A)


