def solution(n):
    answer = 0
    
    for i in range(2, n):
        if n % i == 1:
            answer = i
            break
    
    return answer


# break 안써서 좀 헤맸다.