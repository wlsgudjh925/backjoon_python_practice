n = int(input())
List = [i for i in range(1, n+1)]
stack = []
result = []

for i in range(n):
    arr = int(input())
    if List != []:
        while List[0] <= arr:
            stack.append(List[0])
            List.pop(0)
            result.append('+')
            if List == []:
                break
    if stack[-1] == arr:
        stack.pop()
        result.append('-')

if result.count('-') == n:
    for i in result:
        print(i)
else:
    print('NO')