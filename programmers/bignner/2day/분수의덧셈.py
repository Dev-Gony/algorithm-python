def solution(numer1, denom1, numer2, denom2):
    answer = 0
    numer3 = numer1 * denom2
    numer4 = numer2 * denom1
    numer5 = numer3 + numer4
    denom3 = denom1 * denom2
    
    for i in range(denom3, 1, -1):
        if numer5 % i == 0 and denom3 % i == 0:
            answer = [numer5 // i, denom3 // i]
            break
        else:
            answer = [numer5, denom3]

    return answer


# 2026 02 02 워매 미치것네 