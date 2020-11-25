dp=[[0 for j in range(31)] for i in range(31)]
for j in range(31):
    dp[0][j]=1
for i in range(1,31):
    for j in range(i,31):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

i = 0
while i < 1000:
    n = int(input())
    if n == 0:
        break
    else:
        print(dp[n][n])
    i = i+1