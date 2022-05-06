def pow2(n):
    if n == 1:
        return 2
    return 2 * pow2(n-1)

print(pow2(100))