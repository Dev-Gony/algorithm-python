def solution(numer1, denom1, numer2, denom2):
    answer = 0
    numer3 = numer1 * denom2
    numer4 = numer2 * denom1
    numer5 = numer3 + numer4
    denom3 = denom1 * denom2
    start = max(numer5, denom3)
    for i in range(start, 1, -1):
        if numer5 % i == 0 and denom3 % i == 0:
            answer = [numer5 // i, denom3 // i]
            break
        else:
            answer = [numer5, denom3]

    return answer

# 기약분수를 구하는 알고리즘을 고민을 많이했음.
# 오류가 있는게, 분모로 for문을 돌렸을 때는 테스트케이스 중 2개를 실패
# 분자로 하면 테스트성공임.

# 결론적으로 둘 중에 큰 값으로 모든 값을 돌려봐야하는건데. 그냥 라이브러리 쓰는게 좋아보임.
# 이게 입문문제라는게 말이안되는데... 진짜 다 쉽나?

# # 1. 일단 통분해서 더함
# n = numer1 * denom2 + numer2 * denom1
# d = denom1 * denom2

# # 2. 최대공약수를 찾기 위한 변수 (초기값 1)
# gcd = 1

# # 3. 1부터 두 수 중 작은 수까지 전부 확인 (이게 정석입니다)
# for i in range(1, min(n, d) + 1):
#     if n % i == 0 and d % i == 0:
#         gcd = i  # 공약수를 찾을 때마다 업데이트 (결국 마지막엔 최대공약수가 남음)

# # 4. 딱 한 번만 나누기
# return [n // gcd, d // gcd]
