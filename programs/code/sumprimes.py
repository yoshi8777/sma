def sumprimes(n):
    sum = 0
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(0, len(n)):
        num = n[i]
        if num > 1:
            pr = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    pr = False
                break
            if pr:
                sum = sum + num
            else:
                sum = 0
    return sum


print(sumprimes([3, 3, 1, 13]))
