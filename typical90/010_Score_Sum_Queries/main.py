N = int(input())

A1 = [0] * N
A2 = [0] * N

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        if i == 0:
            A1[i] = P
        else:
            A1[i] = A1[i - 1] + P
        A2[i] = A2[i - 1]
    else:
        if i == 0:
            A2[i] = P
        else:
            A2[i] = A2[i - 1] + P
        A1[i] = A1[i - 1]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        score1 = A1[R - 1] - 0
        score2 = A2[R - 1] - 0
    else:
        score1 = A1[R - 1] - A1[L - 2]
        score2 = A2[R - 1] - A2[L - 2]

    print(score1, score2)
