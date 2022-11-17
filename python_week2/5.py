def solution(absolutes, signs):
    sum_list = []
    if len(absolutes) == len(signs):
        for i in range(0, len(absolutes)):
            if signs[i]:
               sum_list.append(absolutes[i])
            else:
               sum_list.append(-absolutes[i])  
        print(sum_list)       
                   
          
    return sum(sum_list)

print(solution([1,2,3],[True,False,True]))

# 불리언 배열 signs가 매개변수로 주어집니다. 이 문제를 읽어봣어야했는데 거기서 틀렸다
# 불리언 배열로 하면 True False가 아닌 참거짓 그자체로 풀었어야했다. 