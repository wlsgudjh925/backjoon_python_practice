import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic_name = []
dic_num = {}

for i in range(n):
    poke = input().rstrip()
    dic_name.append(poke)
    dic_num[poke] = i + 1

for i in range(m):
    qus = input().rstrip()
    if qus.isdigit():
        print(dic_name[int(qus)-1])
    else:
        print(dic_num[qus])