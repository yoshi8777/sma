def splitsum(l):
    pos_sum = 0
    neg_sum = 0

    for num in l:
        if num > 0:
            pos_sum += num ** 2
        elif num < 0:
            neg_sum += num ** 3

    return [pos_sum, neg_sum]


print(splitsum([1, 3, -5]))  # [10, -125]
print(splitsum([2, 4, 6]))  # [56, 0]
