def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return(answer)

# 사실 두개가 100미만 자연수라고 해서 같은 수끼리 더하면 무조건 2로 나눴을 때, 나머지가 0인 줄 알았는데 99 + 7 도 106이라 오류가 많은 설정이었음
# 나는 바보인가 23 17 도 있고 그냥 널렸네.