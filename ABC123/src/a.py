li = []
for i in range(5):
    li.append(int(input()))

k = int(input())
li = sorted(li)
if k >= li[4] - li[0]:
    print("Yay!")
else:
    print(":(")
