T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    avg = sum(num)/len(num)
    
    print(f"#{test_case}", round(avg))

    # round 함수, 나누기 기호 다시복습
    