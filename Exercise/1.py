# 첫 항이 1이고 공차가 3인 등차수열의 n번째 원소를 구하는 프로그램을 재귀적으로 코딩해보기.
def func(n):
    if n == 1:
        return 1
    else:
        return 3 + func(n-1)

print(func(10))