n, m = map(int, input().split())

dic = {}

for i in range(n):
    a, b = input().split()
    dic[a] = b

for x in range(m):
    c = input()
    print(dic.get(c))