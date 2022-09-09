def sumofdigits(n):
    tot = 0
    while (n > 0):
        dig = n % 10
        tot = tot + dig
        n = n // 10
    return tot

print(sumofdigits(1256))
