def move_zeroes(arr):
    pos = 0

    for i in range(len(arr)):
        if arr[i] !=  0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr

arr = [0, 1, 0, 3, 12, 56, 0, 0, 66, 0, 57, 12]
print(move_zeroes(arr))