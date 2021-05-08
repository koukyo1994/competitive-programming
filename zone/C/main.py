N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]


def is_over_threshold(threshold: int):
    s = set()
    for a in A:
        s.add(sum(1 << i for i in range(5) if a[i] >= threshold))

    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
    return False


lb = 0
ub = 10 ** 9 + 1
while ub - lb > 1:
    thr = (ub + lb) // 2
    if is_over_threshold(thr):
        lb = thr
    else:
        ub = thr

print(lb)
