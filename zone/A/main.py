S = input()

S = S.replace("ZONe", ";")
cnt = 0
for s in S:
    if s == ";":
        cnt += 1

print(cnt)
