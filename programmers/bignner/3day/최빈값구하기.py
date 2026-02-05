def solution(array):
    count_list = [0] * 1000
    for num in array:
        count_list[num] += 1
        
    max_count = max(count_list)
    
    if count_list.count(max_count) > 1:
        return -1
    else:
        return count_list.index(max_count)
    


# 솔직히 어려워서 AI 이용했음.
# 리스트를 1000개의 방으로 만들 생각도 못했고, 마지막에 인덱스값을 찾는거에서도 못했을거같음.
# 이건 자주봐야겠다.