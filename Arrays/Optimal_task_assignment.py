def optimal_task(arr):
    arr.sort()
    time_to_complete_each_task = []
    i = 0
    while i != len(arr)//2:
        time_to_complete_each_task.append(arr[i]+arr[-1-i])
        i += 1

    time_to_complete_each_task.sort()
    return time_to_complete_each_task[-1
    ]


print(optimal_task([6, 2, 3, 7, 5, 5]))
