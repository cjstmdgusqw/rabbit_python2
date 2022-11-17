T = int(input())

for test_case in range(1, T + 1):
    num = map(int, input().split())
    sum = 0
    for i in num:
        if i % 2 != 0:
            sum = sum + i

    print(f"#{test_case}", sum)        