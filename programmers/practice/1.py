#정수 n이 주어질 때, n 이하의 짝수를 모두 더한 값을 구하기


def solution(n):
    for i in n:
        if i % 2 == 0:
            answer += i

    return answer


