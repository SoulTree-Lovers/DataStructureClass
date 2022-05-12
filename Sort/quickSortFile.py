from quickSort import *


def do_sort(input_file):
    data_file = open(input_file)
    A = []

    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)

    for i in range(10):
        print(A[i], end = " ")
    
    print("")

    quickSort(A, 0, len(A)-1)

    for i in range(10):
        print(A[i], end = " ")
    
    print("")

if __name__ == "__main__":
    do_sort("linkbench_short.trc")
