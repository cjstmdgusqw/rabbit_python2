from itertools import combinations

# A = [1,3,5,7]
# cmb = list(combinations(A, 3))
# print(cmb)

def solution(nums):
    count = 0
    new_list = list(combinations(nums, 3))
    for i in range(len(new_list)):
       pass

print(solution([1,2,3,4]))        