def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer

# 처음에 그냥 / 로 했는데, 실패해서 //로 했는데, 또 실패해서 예시를 살펴봤더니 순환소수여서 정수부분만 살려야 한다는 걸 확인