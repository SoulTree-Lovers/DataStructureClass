import sys
sys.path.append("..")

from LinkedList.circularDoublyLinkedList import *

def do_sim(cache_slots):
    cache_hit = 0
    cache_miss = 0  # 캐시 미스 추가
    tot_cnt = 0
    
    data_file = open("linkbench_short.trc")
    
    # 캐시 슬롯 리스트 생성
    cache_slot = CircularDoublyLinkedList()

    # 캐시 사이즈를 입력값에 따라 제한
    cache_size = cache_slots
    
    for line in data_file.readlines():
        lpn = line.split()[0]

        # 캐시 슬롯 리스트에 찾는 값이 없는 경우
        if lpn not in cache_slot:
            if cache_slot.size() < cache_size:  # 캐시 슬롯 리스트의 길이가 제한값보다 작은 경우
                cache_slot.append(lpn)          # 캐시 슬롯에 데이터 추가
                cache_miss += 1                 # 캐시 미스 + 1
                tot_cnt += 1                    # 전체 카운트 + 1

            else:                               # 캐시 슬롯 리스트의 길이가 제한값보다 큰 경우
                cache_slot.pop(0)               # 가장 오래 사용하지 않은 데이터 삭제
                cache_slot.append(lpn)          # 캐시 슬롯에 데이터 추가
                cache_miss += 1                 # 캐시 미스 + 1
                tot_cnt += 1                    # 전체 카운트 + 1

        # 캐시 슬롯 리스트에 찾는 값이 있는 경우
        else:
            cache_slot.pop(cache_slot.index(lpn))   # 일치하는 데이터 삭제
            cache_slot.append(lpn)                  # 데이터를 가장 최근 위치에 추가
            tot_cnt += 1                            # 전체 카운트 + 1        
            cache_hit += 1                          # 캐시 히트 + 1

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "cache_miss = ", cache_miss, "hit ratio = ", cache_hit / tot_cnt)   

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)