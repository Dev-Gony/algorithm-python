def solution(n):
    answer = 0
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = (n // 7) + 1
    return answer


# 1명한테 1조각씩은 너무하네 2~3조각은 줘라