def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


arr = [1, 2, 5, 7, 2, 3, 4, 4, 1]
print(remove_duplicates(arr))