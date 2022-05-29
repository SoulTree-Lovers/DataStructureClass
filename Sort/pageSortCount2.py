from mergeSort import *

def do_sort(input_file):
    cnt = dict()
    data_file =open(input_file)
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn in cnt:
            cnt[lpn]+=1
        else:
            cnt[lpn]=1
    count =[]

    for item in cnt:
        count.append(cnt[item])
    
    
    mergeSort(count, 0, len(count) - 1)
    
    count.reverse()

    for i in range(10):
        for item in cnt:
            if cnt[item] == count[i]:
                print(item, count[i])
                del cnt[item]
                break
 
do_sort("linkbench_short.trc")