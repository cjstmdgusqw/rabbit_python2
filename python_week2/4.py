def solution(n):
    A = []
    for i in range(1, n+1):
        if n % i == 1:
            A.append(i)
            

    return min(A)

print(solution(12))    