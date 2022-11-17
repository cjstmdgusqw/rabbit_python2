# 두 정수의 합

# def solution(a, b):
#     sum = 0
#     if a < b: 
#         for i in range(a, b+1):
#             sum = sum + i
#         return sum
#     else:
#         for j in range(b, a+1):
#             sum = sum + j
#         return sum    
         
# solution(5,3)

def solution(a,b):
    A = sum(range(min(a,b),max(a,b)+1))
    return A


print(solution(5,3))