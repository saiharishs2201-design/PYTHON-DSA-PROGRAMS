from itertools import permutations

nums = list(map(int, input("Enter numbers: ").split()))

print("Permutations:")
for p in permutations(nums):
    print(p)