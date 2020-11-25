count = int(input())
stack = []
for i in range(0, count):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))