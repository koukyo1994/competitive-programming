N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

max_a = max(As)
min_b = min(Bs)

if min_b < max_a:
    print(0)
else:
    print(min_b - max_a + 1)
