arr = list(map(int, input("Enter array: ").split()))

largest = float('-inf')
second = float('-inf')

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

if second == float('-inf'):
    print("No second largest element")
else:
    print("Second largest:", second)