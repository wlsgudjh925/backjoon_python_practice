n = int(input())
good_word = 0

for i in range(n):
    string = input().rstrip()
    stack = []
    for i in string:
        if stack == []:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if stack == []:
        good_word = good_word + 1

print(good_word)