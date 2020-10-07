stack = []
book = dict()
for i in range(int(input())):
    name = input()
    if name not in book.keys():
        book[name] = 1
    else:
        book[name] += 1

best = max(book.values())

for name, value in book.items():
    if best == value:
        stack.append(name)

stack.sort()
print(stack[0])