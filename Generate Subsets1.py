def subsets(nums):
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


nums = list(map(int, input("Enter numbers: ").split()))

print("Subsets:")
for s in subsets(nums):
    print(s)