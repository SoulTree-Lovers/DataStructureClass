# fibonacci 수열을 재귀에서 for문으로 바꾸기
def fibo(n):
    if n <= 2:
        return 1

    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a + b

    return b

for i in range(1, 11):
    print("fibo({}) = {}".format(i, fibo(i))) 