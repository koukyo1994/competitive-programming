N, L = list(map(int, input().split()))
K = int(input())
As = list(map(int, input().split()))

ub = int(L / K) if L % K == 0 else int(L / K) + 1
lb = 0
while ub - lb > 1:
    mid = int((ub + lb) / 2)
    previous = -1
    current = 0
    can_cut = True
    for i in range(K):
        if previous == -1:
            pos_prev = 0
        else:
            if len(As) <= previous:
                break
            else:
                pos_prev = As[previous]

        if len(As) <= current:
            can_cut = False
            break
        pos_cur = As[current]
        while pos_cur - pos_prev < mid:
            current += 1
            if len(As) <= current:
                can_cut = False
                break
            pos_cur = As[current]
        previous = current
        if i == K - 1:
            if can_cut:
                if L - As[current] < mid:
                    can_cut = False
    if can_cut:
        lb = mid
    else:
        ub = mid

print(lb)
