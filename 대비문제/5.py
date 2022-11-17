T = int(input())
num = list(map(int, input().split()))
num.sort()
    

for i in range(T):
    if i == T//2:
        print(num[i])
        break
    
