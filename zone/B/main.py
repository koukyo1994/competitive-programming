N, D, H = list(map(int, input().split()))
seppen = []
for i in range(N):
    d, h = list(map(int, input().split()))
    slope = (H - h) / (D - d)
    s = H - slope * D
    if s < 0:
        s = 0.0
    seppen.append(s)

print(max(seppen))
