def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_partition(m):
    if m <= 0:
        return False
    for i in range(2, m):
        if is_prime(i) and is_prime(m - i):
            return True
    return False


res=prime_partition(185)
print(res)