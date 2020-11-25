import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(n):
    poke = input()
    dic[i+1] = poke

for i in range(m):
    qus = input()
    try:
        print(dic[int(qus)])
    except:
        for i in dic:
            if dic[i] == qus:
                print(i)

