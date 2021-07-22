N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

inconvenience = 0
for i in range(N):
    inconvenience += abs(A[i] - B[i])

print(inconvenience)
