def second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        return None

    return second


# Example
arr = [-12,-3,1,-1,0,-6,2]
print(second_largest(arr))