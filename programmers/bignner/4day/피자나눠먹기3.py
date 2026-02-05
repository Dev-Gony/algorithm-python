def solution(slice, n):
    answer = 0
    
    if slice > n:
        answer = 1
    elif n % slice == 0:
        answer = n // slice
    else:
        answer = (n // slice) + 1
            
    return answer


# 처음에 슬라이스와 인원수가 주어지고, 같은 수 만큼 먹는 건줄 알고, slice가 1부터 10까지니까 저 조건으로 조건문 10개 만들어야하는줄...