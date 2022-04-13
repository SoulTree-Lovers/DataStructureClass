from ListStack import *

def evaluate(postfix):
    s = ListStack()
    digitPreviously = False

    for i in range(len(postfix)):
        ch = postfix[i] # i번 문자. 번호는 0번부터
        if ch.isdigit():    # ch가 숫자
            # 연속된 숫자를 합치는 과정
            if digitPreviously:
                tmp = s.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                s.push(tmp)
            else:
                s.push(ord(ch) - ord('0'))
                digitPreviously = True
        elif isOperator(ch):    # ch가 연산자
            s.push(operation(s.pop(), s.pop(), ch))   # 두 숫자를 꺼내어 계산
            digitPreviously = False
        else:   # ch가 공백
            digitPreviously = False
    return s.pop()

def isOperator(ch) -> bool:     # 연산자인가?
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2:int, opr1:int, char) -> int:   # 연산하기
    # 실제 계산하는 부분 (switch/case문 대신 dictionary 활용)
    oper_dict = {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}
    return oper_dict[char]

def main():
    postfix = "700 3 47 + 6 * - 4 /"    # 테스트 샘플 입력 (후위 표현식)
    print("input string: ", postfix)
    answer = evaluate(postfix)
    print("Answer:", answer)
    print(ord('0'), ord('9'))

if __name__ == "__main__":
    main()

