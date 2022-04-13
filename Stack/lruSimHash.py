from LRU_hashtable import *

def do_sim(cache_slots):
    cache_hit = 0
    cache_miss = 0
    tot_cnt = 0
    
    data_file = open("linkbench_short.trc")
    
    # 캐시 슬롯 리스트 생성
    cache_slot = LRUCache(cache_slots)
    
    
    for line in data_file.readlines():
        lpn = line.split()[0]

        if lpn == cache_slot.get(lpn):
            cache_slot.put(lpn, lpn)
            cache_hit += 1
            tot_cnt += 1
        else:
            cache_slot.put(lpn, lpn)
            cache_miss += 1
            tot_cnt += 1
        
    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "cache_miss = ", cache_miss, "hit ratio = ", cache_hit / tot_cnt)   

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)