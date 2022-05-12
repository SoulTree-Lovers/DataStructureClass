from quickSort import *
from mergeSort import *

def do_sort(input_file):
    data_file = open(input_file)
    A = []

    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
    
    count = {}
    values = []

    for y in range(len(A)-1):
        x = y
        while A[x] == A[y]:
            if  A[x] not in list(count.keys()):
                count[A[x]] = 1
                x += 1
            elif A[x] in list(count.keys()):
                count[str(A[x])] += 1
                x += 1

    for i in range(len(count)):
        values.append(list(count.values())[i])

    mergeSort(values, 0, len(values)-1)

    reverseCount = dict(map(reversed, count.items()))

    newValues = []    
    keys = []

    for i in range(len(values)-1, len(values)-11, -1):      # value 리스트의 뒤에서 10개 추출
        newValues.append(values[i])
        keys.append(reverseCount.get(values[i]))
    
    for i in range(10):
        print("{} : {}".format(keys[i], newValues[i]))

if __name__ == "__main__":
    do_sort("linkbench_short.trc")