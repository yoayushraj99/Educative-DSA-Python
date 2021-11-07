def advance_game(A):
    furthest_reached = 0
    lst_idx = len(A) - 1
    i = 0
    while i <= furthest_reached < lst_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1

    return furthest_reached >= lst_idx


print(advance_game([3, 3, 1, 0, 2, 0, 1]))
print(advance_game([3, 2, 0, 0, 2, 0, 1]))
