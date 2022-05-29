from mergeSort import *

def do_sort(input_file):
    data_file = open(input_file)
    A = []

    # 파일을 읽고 리스트에 추가
    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
    
    # 카운트를 저장할 딕셔너리와 빈 리스트 생성
    count = {}
    values = []

    # 카운트 딕셔너리에 키-값 형태로 개별 카운트 개수 저장
    for y in range(len(A)-1):
        x = y
        while A[x] == A[y]:
            if  A[x] not in list(count.keys()):
                count[A[x]] = 1
                x += 1
            elif A[x] in list(count.keys()):
                count[str(A[x])] += 1
                x += 1

    # 아까 생성한 값 리스트에 카운트에 저장되었던 값(각 수의 갯수) 추가
    for i in range(len(count)):
        values.append(list(count.values())[i])  

    # mergeSort를 이용하여 값 리스트 정렬 
    mergeSort(values, 0, len(values)-1)      # quickSort 대신 mergeSort 사용

    # 기존 카운트 딕셔너리의 키와 값을 서로 바꿈
    reverseCount = dict(map(reversed, count.items()))

    # 빈 리스트 두 개 생성
    newValues = []    
    keys = []

    # values 리스트에서 키와 값을 큰 순서대로 10개씩 추출
    for i in range(len(values)-1, len(values)-11, -1):      # value 리스트의 뒤에서 10개 추출
        newValues.append(values[i])
        keys.append(reverseCount.get(values[i]))

    # 수와 카운트 출력
    for i in range(10):
        print("{} : {}".format(keys[i], newValues[i]))

if __name__ == "__main__":
    do_sort("linkbench_short.trc")