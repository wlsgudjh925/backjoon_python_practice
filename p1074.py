def func(n, x, y):
    if n == 1:
        if x == 0 and y == 0:
            return 0
        elif x == 1 and y == 0:
            return 1
        elif x == 0 and y == 1:
            return 2
        elif x == 1 and y == 1:
            return 3
    else:
        half = 2 ** (n-1)
        if x >= half and y >= half:
            return 4 ** (n-1) * 3 + func(n-1, x-half, y-half)
        elif x >= half and y < half:
            return 4 ** (n-1) + func(n-1, x-half, y)
        elif x < half and y >= half:
            return 4 ** (n-1) * 2 + func(n-1, x, y-half)
        elif x < half and y < half:
            return func(n-1, x, y)

n,a,b = map(int, input().split())
print(func(n,b,a))