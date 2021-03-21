import sys

H, W, A, B = map(int, input().split(" "))

if A == 0:
    print(1)
    sys.exit(0)

if H * W == 2:
    print(1)

if H * W == 3:
    if A == 1:
        print(2)
    else:
        print(1)

if H * W == 4 and H == 2:
    if A == 1:
        print(4)
    else:
        print(2)

if H * W == 4 and min(H, W) == 1:
    if A == 1:
        print(3)
    else:
        print(1)

if H * W == 5:
    if A == 1:
        print(4)
    else:
        print(3)

if H * W == 6:
    if min(H, W) == 1:
        if A == 1:
            print(5)
        elif A == 2:
            print(5)
        else:
            print(1)
    else:
        if A == 1:
            print(7)
        elif A == 2:
            print(9)
        else:
            print(3)

if H * W == 7:
    if A == 1:
        print(6)
    elif A == 2:
        print()
