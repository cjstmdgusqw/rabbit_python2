# num = int(input())

# for i in range(1, num+1):
#     A = str(i).replace("3", "-")
#     B = A.replace("6", "-")
#     C = B.replace("9", "-")
#     print(C, end=' ')
    
# 문제이해도도 중요함...


T = int(input())
for i in range(1, T+1): # 1 ~ 100

    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')