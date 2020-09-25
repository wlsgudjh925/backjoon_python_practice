testcount = int(input())
test = 0

while test < testcount:
    ans = input().strip()
    score = 0
    stack = []
    for j in ans:
        if j == 'O':
            score = score + 1 + stack.count('O')
            stack.append(j)
        elif j == 'X':
            stack = []
    print(score)
    test = test + 1