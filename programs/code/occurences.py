def remdup(l):
    result = []
    seen = set()

    for num in reversed(l):
        if num not in seen:
            result.append(num)
            seen.add(num)
    return list(reversed(result))


print(remdup([3, 1, 3, 5]))  # [1, 3, 5]
print(remdup([7, 3, -1, -5]))  # [7, 3, -1, -5]
