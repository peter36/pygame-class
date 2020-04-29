def find_max(arr):
    max = arr[0]
    n = len(arr)
    for i in range(0, n):
        if arr[i] > max:
            max = arr[i]
    return max


a = [325, 123, 21, 52, 789, 2, 32]
m = find_max(a)
print(m)
