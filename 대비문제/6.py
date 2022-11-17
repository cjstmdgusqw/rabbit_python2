num = input()
A = []
for i in num:
    A.append(i)
    A_list = map(int,A)
print(sum(A_list))
