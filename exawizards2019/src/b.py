N = int(input())

s = list(input())

cnt = 0
for i in s:
    if i == "R":
        cnt += 1

blu = N - cnt
if cnt > blu:
    print("Yes")
else:
    print("No")
