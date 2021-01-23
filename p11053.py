N = int(input())

A = list(map(int,input().split()))
DP = [1] * N

for i in range(N):
    cur = A[i]
    for j in range(i):
        before = A[j]
        if cur > before: # 현재 값이 이전에 있는 값보다 클 경우
            DP[i] = max(DP[i], DP[j]+1)

DP.sort()
print(DP[-1])