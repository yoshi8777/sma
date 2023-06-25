def reverse(n):
    a = ""

    while n > 0:
        b = str(n % 10)
        a = a + b
        n = n // 10
    return int(a)


print(reverse(783))
