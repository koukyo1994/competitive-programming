N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

li = [(A, 0), (B, 1), (C, 2), (D, 3), (E, 4)]
bottleneck = min(li, key=lambda x: x[0])
t = 0
import ipdb
ipdb.set_trace()
t += bottleneck[1]
b = bottleneck[0]
if N % b == 0:
    t += N / b
else:
    t += N // b + 1
t += 4 - bottleneck[1]
print(t)
