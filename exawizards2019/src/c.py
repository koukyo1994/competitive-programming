N, Q = list(map(int, input().split()))
s = input()

char = {}
for i, c in enumerate(s):
    if c not in char.keys():
        char[c] = [i]
    else:
        char[c] = char[c] + [i]

count = [1] * N
out = 0
for _ in range(Q):
    A, L = input().split()
    try:
        idx = char[A]
    except KeyError:
        continue

    if L == "L":
        for ix in idx:
            temp = count[ix]
            count[ix] = 0
            if ix == 0:
                out += temp
            else:
                count[ix - 1] += temp
    else:
        for ix in idx:
            temp = count[ix]
            count[ix] = 0
            if ix == N - 1:
                out += temp
            else:
                count[ix + 1] += temp

print(N - out)
