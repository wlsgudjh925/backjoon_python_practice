while 1:
    string = input().rstrip()
    stack = []
    balance = 1
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balance = 0
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balance = 0
                break
    if string == '.':
        break
    if len(stack) == 0 and balance == 1:
        print("yes")
    else:
        print("no")