def rotatelist(l, k):
    if k <= 0:
        return l
    rotate_count = k % len(l)
    rotated_list = l[rotate_count:] + l[:rotate_count]

    return rotated_list


print(rotatelist([1, 2, 3, 4, 5], 1))  # [2, 3, 4, 5, 1]
print(rotatelist([1, 2, 3, 4, 5], 3))  # [4, 5, 1, 2, 3]
