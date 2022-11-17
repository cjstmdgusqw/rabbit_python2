N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
A = len(stages)

for i in range(1,N+1):
    fail_percent = stages.count(i)/A
    A = A - stages.count(i)
    print(i, fail_percent)
    # print(stages.count(i))

    #흐음..여기서 순서대로 어떻게 해야하나...
             