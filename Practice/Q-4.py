# Find runner up score

n = 5
arr = [2, 3, 6, 6, 5]

def runner_up(arr):

    max_num = 0

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num

print(runner_up(arr))