T = int(input())
for i in range(T):
    string = input().rstrip()
    stack = []
    balance = 1

    for j in string:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack != [] and stack[-1] == '(':
                stack.pop()
            else:
                balance = 0

    if stack == [] and balance == 1:
        print("YES")
    else:
        print("NO")