N = int(input())
A = sorted(list(map(int, input().split())))


def binary_search(B: int, A: list):
    ub = len(A)
    lb = 0
    while ub - lb > 1:
        mid = int((lb + ub) // 2)
        if B >= A[mid]:
            lb = mid
        else:
            ub = mid
    return lb


def get_distance(B: int, lb: int, A: list):
    if lb == len(A) - 1:
        return abs(B - A[lb])
    elif lb == 0:
        return abs(B - A[lb])
    else:
        return abs(min(B - A[lb], A[lb + 1] - B))


Q = int(input())
for i in range(Q):
    B = int(input())
    lb = binary_search(B, A)
    print(get_distance(B, lb, A))
