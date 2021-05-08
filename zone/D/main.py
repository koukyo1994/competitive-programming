from collections import deque

S = input()

is_reversed = False
T = deque()
for c in S:
    if c == "R":
        is_reversed = not is_reversed
    elif is_reversed:
        if T and c == T[0]:
            T.popleft()
        else:
            T.appendleft(c)
    else:
        if T and c == T[-1]:
            T.pop()
        else:
            T.append(c)

if is_reversed:
    T = list(reversed(T))

print("".join(T))
