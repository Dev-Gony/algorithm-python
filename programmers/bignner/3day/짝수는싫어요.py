def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer


# 간단한데, 다른 방법이 뭐가있으려나 흠...