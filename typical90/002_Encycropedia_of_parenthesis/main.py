import itertools

N = int(input())

if N % 2 == 1:
    import sys
    sys.exit(0)


def score(slist: tuple):
    cnt = 0
    for i in slist:
        if cnt < 0:
            return False
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
    return cnt == 0


vocab = "()"
for v in itertools.product(vocab, repeat=N):
    if score(v):
        print("".join(v))
    else:
        pass
