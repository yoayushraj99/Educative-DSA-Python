def intersection(arr1, arr2):
    i, j = 0, 0
    common = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] != arr1[i-1] or i == 0:
                common.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common


print(intersection([2, 3, 3, 5, 7 ,11], [3, 3, 7 ,15, 31]))
