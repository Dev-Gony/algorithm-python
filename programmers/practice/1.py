#정수 n이 주어질 때, n 이하의 짝수를 모두 더한 값을 구하기


def solution(n):
    for i in n:
        if i % 2 == 0:
            answer += i

    return answer


def solution(n):
    answer = 0  # 1. 먼저 0으로 시작한다고 알려주기!
    
    # 2. 1부터 n까지 숫자를 하나씩 꺼내기 위해 range 사용
    # n 이하(n까지 포함)니까 n + 1을 해줘야 해요.
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i
            
    return answer

# ---

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer



# ---

# 문제 설명: 정수 리스트 num_list가 매개변수로 주어집니다. num_list의 원소 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예: [1, 2, 3] -> [3, 2, 1]

def solution(num_list):
    reverse_list = []
    reverse_list = sorted(reverse=True)

    return reverse_list

# 개틀림
# ---
#for문과 if를 복습해 볼까요? 문제: 리스트 array와 숫자 n이 주어질 때, array 안에 n이 몇 개 있는지 맞히는 문제입니다.

def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

# ---

# 문제 설명: 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers.sort()
    a = max(numbers)
    numbers.pop()
    b = max(numbers)
    return a * b

# 굳이 이렇게 말고
# mubers.sort()
# return numbers[-1] * numbers[-2]
# 이게 더 간편
# ---

# 문제 설명:정수 n이 매개변수로 주어질 때 n의 각 자릿수의 합을 return하도록 solution 함수를 완성해주세요.입출력 예: 1234 -> $1 + 2 + 3 + 4 = 10$
# ---

# ---

# ---

# ---

# ---

# ---

