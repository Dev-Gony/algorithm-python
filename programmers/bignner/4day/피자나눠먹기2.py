def solution(n):
    answer = 0
    
    if n % 6 == 0:
        answer = n // 6
    elif n % 2 == 0:
        answer = ((6 * n) // 2) // 6
    elif n % 3 == 0:
        answer = ((6 * n) // 3) // 6
    else:
        answer = (6 * n) // 6
    
    return answer


# 최소공배수 구하는 문제
# 최대공약수를 한 번 맛봐서그런지 고민하다보니 풀림. 신기하군