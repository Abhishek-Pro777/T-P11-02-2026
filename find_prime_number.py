num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
        break
if flag:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")