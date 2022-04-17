# 다음 하노이 탑 재귀 알고리즘에 대해 5개의 원반을 옮기고자 move(5, a, b, c)를 수행하면
# 함수 move()는 총 몇 회 호출되는가? 이때 최초의 호출 move(5, a, b, c)도 포함하여 센다.
# 원반을 옮기는 횟수와 move()가 호출되는 횟수는 같지 않다.
# (03번 문제처럼 피해갈 수 있는데도 재귀를 통해 중복 호출을 하는 예도 있다. 이번 문제는
# 피해갈 수 없지만 호출이 지수함수적으로 증가하는 하노이 탑 문제의 호출 횟수를 느껴보려는 것이다.)

MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"


def move(N, start, destination):
    print(MOVE_MESSAGE.format(N, start, destination))


def hanoi(n, start, destination, via):
    """
    하노이의 탑 규칙에 따라 원반을 옮기고,
    옮길 때마다 원반의 시작 위치와 이동한 위치를 출력합니다.
    마지막으로 총 이동 횟수를 반환합니다.
    :params
        n: 총 원반 개수
        start: 시작 기둥
        destination: 도착 기둥
        via: 보조 기둥:
    :return count:
    """
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        move(1, start, destination)
        return 1

    count = 0
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
    count += hanoi(n - 1, start, via, destination)

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    count += 1
    move(n, start, destination)

    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동
    count += hanoi(n - 1, via, destination, start)

    return count


if __name__ == '__main__':
    n = 5
    start = 1
    destination = 3
    via = 2

    total_count = hanoi(n, start, destination, via)
    print('총 이동 횟수:', total_count)

# 총 이동 횟수 : 31회

# 05번 
# move 함수 호출 횟수 : 원반 옮기는 횟수 + 1 = 31 + 1 = 32회

# 06번
# 경계 조건이 없다면 재귀적으로 move() 함수를 무한으로 호출하여 에러가 발생한다.