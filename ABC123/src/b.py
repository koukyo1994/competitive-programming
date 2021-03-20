li = []

for i in range(5):
    li.append(int(input()))

res = []
for i in range(5):
    if li[i] % 10 == 0:
        res.append((0, li[i]))
    else:
        res.append((((li[i] // 10 + 1) * 10 - li[i]), li[i]))
res.sort(key=lambda x: x[0])

cnt = 0
for i, j in res[:4]:
    cnt += i + j

cnt += res[4][1]
print(cnt)
