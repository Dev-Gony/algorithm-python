def solution(array):
    answer = 0
    array = sorted(array)
    answer = array[int(len(array)/2)]
    return answer


# 중앙값이라는게 무슨 말인가 했네.
# 어차피 홀수 고정이니까 나누면 0.5는 무조껀 떨어진다고 생각했고
# 정수로만 받으면 뒷자리 잘리면서 해당 정수로 리스트위치 표시하면 중앙값된다고 생각