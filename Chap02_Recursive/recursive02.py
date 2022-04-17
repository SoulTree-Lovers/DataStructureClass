# 본문에서 소개한 다음 알고리즘에서 양의 정수 n에 대해 함수 seq()는 총 몇 회 호출되는가?
# 이때 최초의 호출 seq(n)도 포함하여 센다.

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3

# 함수 하나 당 재귀적으로 함수 하나가 실행되므로 n번
# ex) n=1 일때 seq(1)만 호출되므로 1번 호출
# ex) n=2 일때 seq(2), seq(1)이 호출되므로 2번 호출
# ...
# 답 : n번 호출된다.