arr = list(map(int, input("Enter array: ").split()))

count = 0
n = len(arr)

for i in range(n):
    if arr[i] > arr[(i + 1) % n]:
        count += 1

if count <= 1:
    print("Array is sorted and rotated")
else:
    print("Array is not sorted and rotated")