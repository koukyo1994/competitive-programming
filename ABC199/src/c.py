def swap(S: list, N: int):
    return S[N:] + S[:N]


def swap_letter(S: list, a: int, b: int):
    a_letter = S[a - 1]
    b_letter = S[b - 1]
    S[a - 1] = b_letter
    S[b - 1] = a_letter
    return S


N = int(input())
S = list(input())
Q = int(input())

is_reversed = False
for i in range(Q):
    T, A, B = list(map(int, input().split()))
    if T == 2:
        is_reversed = not(is_reversed)
    else:
        if is_reversed:
            if A < N:
                A_ = A + N
            else:
                A_ = A - N

            if B < N:
                B_ = B + N
            else:
                B_ = B - N
            S = swap_letter(S, A_, B_)
        else:
            S = swap_letter(S, A, B)

if is_reversed:
    S = swap(S, N)

print("".join(S))
