T = int(input())
DP = [0, 1, 2, 4]
for i in range(4, 11):
    DP.append(DP[i-3]+DP[i-2]+DP[i-1])

for i in range(T):
    n = int(input())
    print(DP[n])