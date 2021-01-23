N, M = map(int, input().split())
maze = []
DP = [[0 for i in range(M+1)] for i in range(N+1)]

for i in range(N):
    maze.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        result = max(max(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1])
        DP[i][j] = result + maze[i-1][j-1]

print(DP[N][M])