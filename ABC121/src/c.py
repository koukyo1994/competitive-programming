num = input()
N, M = [int(x) for x in num.split()]

dic = []
for n in range(N):
    num = input()
    a, b = [int(x) for x in num.split()]
    dic.append((a, b))

sort = sorted(dic, key=lambda x: x[0])
count = 0
money = 0
ind = 0
while count < M:

    if (M - count) > sort[ind][1]:
        money += sort[ind][0] * sort[ind][1]
        count += sort[ind][1]
    else:
        money += sort[ind][0] * (M - count)
        count += (M - count)

    ind += 1
print(money)
