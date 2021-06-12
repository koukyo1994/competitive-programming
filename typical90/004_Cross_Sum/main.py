H, W = list(map(int, input().split()))
sum_rows = []
sum_cols = [0] * W

A = []
for i in range(H):
    row = list(map(int, input().split()))
    sum_rows.append(sum(row))
    for j in range(W):
        sum_cols[j] += row[j]
    A.append(row)


for i in range(H):
    for j in range(W):
        print(f"{sum_rows[i] + sum_cols[j] - A[i][j]} ", end="")
        if j == W - 1:
            print("")
