string = input().rstrip()
count = 0
before = 0
stack = []

for i in string:
    if i == '(':
        stack.append(i)
    elif before == '(' and i == ')':
        stack.pop() #레이저는 스택(쇠막대기)에 포함되지 않으므로 '(' 를 뺌
        count += len(stack)
    elif before == ')' and i == ')':
        stack.pop()
        count += 1
    before = i

print(count)
