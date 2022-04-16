import sys
sys.path.append("..")

from linkedQueue import LinkedQueue

class sentenceChecker():
    """$를 기준으로 앞, 뒤 문자열이 같은지 확인해주는 클래스"""    
    def __init__(self):
        """연결리스트를 이용한 큐 클래스 사용"""
        self.__queue = LinkedQueue()
    
    def is_included(self, s):
        """앞, 뒤 문자열이 같은지 확인해주는 메소드"""
        index = s.find('$')     # $의 인덱스 찾기

        for i in range(index):  
            self.__queue.enqueue(s[i])      # $의 앞 문자열을 큐에 입력  
        
        for i in range(index+1, len(s)):     
            prev = self.__queue.dequeue()   # $의 뒤 문자열을 앞 문자열과 하나씩 비교 후 큐에서 제거
            curr = s[i]
        
            if prev != curr:
                return False                # 앞, 뒤 문자열이 하나라도 다르면 False 리턴
        
        return self.__queue.isEmpty()       # 최종적으로 큐에 문자열이 남아있는지 확인
    
if __name__ == "__main__":
    s = "abc$abc"
    checker = sentenceChecker()
    rv = checker.is_included(s)

    if rv == True:
        print("included")
    else:
        print("Not included")