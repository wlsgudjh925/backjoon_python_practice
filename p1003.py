def count_fi(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if n < 3: #0, 1, 2일 경우는 이미 만들어져 있으므로
        return

    for i in range(3, n+1):
        zero.append(zero[-1]+zero[-2])
        one.append(one[-1]+one[-2])

    return zero, one

zero, one = count_fi(40)

t = int(input())

for j in range(t):
    n = int(input())
    print(zero[n], one[n])