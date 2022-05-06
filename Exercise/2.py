# 하노이 타워 문제 코딩
def move(n, start, destination, temp):
    if n > 0:
        move(n-1, start, temp, destination)
        print("move {} from {} to {}".format(n, start, destination))
        move(n-1, temp, destination, start)

move(3, "a", "b", "c")