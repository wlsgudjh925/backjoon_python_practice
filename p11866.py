n, k = map(int, input().split())
inp = []
out = []
a = 1
b = -1

for i in range(1, n+1):
    inp.append(i)

while len(inp) != 1:
    x = len(inp)
    while k*a+b <= x:
        out.append(inp[k*a+b])
        print(inp)
        a = a + 1
        if k*a+b == x:
            break
    for i in out:
        if inp.count(i) == 1:
            inp.remove(i)
    a = 0
    b = x % k

out.append(inp[0])
print('<'+", ".join(map(str, out))+'>')