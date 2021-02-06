N = int(input())
s = list(map(int, input().split()))
DP = [1] * N

for i in range(N):
    cur = s[i]
    for j in range(i):
        before = s[j]
        if cur < before:
            DP[i] = max(DP[i], DP[j]+1)

print(N - max(DP))
