arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

n = len(arr)
k = k % n

arr = arr[-k:] + arr[:-k]

print("Rotated array:", arr)