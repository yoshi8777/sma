def flatten(l):
    result = []

    for item in l:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten([1, 2, [3], [4, [5, 6]]]))
# Output: [1, 2, 3, 4, 5, 6]
