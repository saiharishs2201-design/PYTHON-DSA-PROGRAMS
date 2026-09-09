def remove_duplicates(arr):
    result = []
    seen = set()

    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)

    return result

print(remove_duplicates([1,2,2,3,1,4,3,4]))