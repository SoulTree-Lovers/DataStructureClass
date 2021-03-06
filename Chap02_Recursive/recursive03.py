# 다음 피보나치 수열을 구하는 재귀 알고리즘에서 5번째 피보나치 수를 구하는 fib(5)를 수행하면
# 함수 fib()는 총 몇 회 호출되는가? 이때 최초의 호출 fib(5)도 포함하여 센다.
# (이 문제는 fib()가 매우 불필요한 중복 호출이 심하다는 것을 느껴보려는 것이다.)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# fib(5)를 실행하면,
# fib(4) + fib(3),
# fib(3) + fib(2) / fib(2) + fib(1)
# fib(2) + fib(1)

# 이렇게 총 9번 호출된다.