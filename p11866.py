n, k = map(int, input().split())

que = []

for i in range(n):
    que.append(i+1)

print("<", end="")

while len(que) != 0:
    for i in range(k-1):
        que.append(que[0])
        que.pop(0)
    if len(que) != 1:
        print(que[0], end="")
        print(",", end=" ")
    else:
        print(que[0], end="")
    que.pop(0)

print(">", end="")