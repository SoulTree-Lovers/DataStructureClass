# fibonacci 수열을 재귀에서 for문으로 바꾸기
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        listA = [1, 1]
        for i in range(n-2):
            listA.append(listA[i]+listA[i+1])
        return listA[-1]

print("fibo(1): ", fibo(1))
print("fibo(2): ", fibo(2))
print("fibo(3): ", fibo(3))
print("fibo(4): ", fibo(4))
print("fibo(5): ", fibo(5))