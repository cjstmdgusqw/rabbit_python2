# day = int(input())
# for i in range(1,day+1):
num = int(input())
for j in range(0, num):
    num_day = list(map(int, input().split()))
    print(max(num_day))
    if num_day[j] == max(num_day):
        num_day.remove(num_day[j])


    