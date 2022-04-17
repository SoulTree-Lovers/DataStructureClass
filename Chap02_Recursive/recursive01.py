# 다음 수열의 n번째 항을 구하는 재귀 알고리즘을 작성하시오.
# an = 5a(n-1) + 3, a1 = 0

def recursive(n):
    if n == 1:
        return 0
    else:
        return 5 * recursive(n-1) + 3


print("recursive(1):", recursive(1))
print("recursive(2):", recursive(2))
print("recursive(3):", recursive(3))
print("recursive(4):", recursive(4))
print("recursive(5):", recursive(5))
