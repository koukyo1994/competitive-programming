N = input()
if int(N) <= 10:
    print(0)
else:
    if len(N) % 2 == 1:
        lenN = len(N)
        nines = "9" * (lenN - 1)
        N = nines
    half = len(N) // 2
    n = int(N[:half])
    n_ = int(N[half:])
    if n_ >= n:
        print(n)
    else:
        print(n - 1)
