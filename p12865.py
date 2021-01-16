N, K = map(int, input().split())
obj = [[0, 0]]

for i in range(N):
    obj.append(list(map(int, input().split()))) #2차원 배열로 저장

backpack = [[0 for i in range(K+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W = obj[i][0]
        V = obj[i][1]
        if j >= W: #기존의 무게보다 크거나 같을 경우
            backpack[i][j] = max(backpack[i-1][j], backpack[i-1][j-W] + V)
        else:
            backpack[i][j] = backpack[i-1][j] #작다면 그대로

print(backpack[N][K]) #우측하단에 있는 숫자가 최대값