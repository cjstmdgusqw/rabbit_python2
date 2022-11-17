#정수 내림차순으로 배치하기
def solution(n):
    A = list(str(n))
    A.sort(reverse=True)
    return (''.join(A))

print(solution(118372))

# some_list = [5, 7, 2, 3, 1]

# print(sorted(some_list))
# print(some_list.sort())

# sort와 sorted의 차이
# join 사용 쓰는법은 아는데 너무 오랜만이라...ㅎㅎ