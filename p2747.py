n = int(input())
fi = [0, 1]

for i in range(1, n):
    fi.append(fi[i]+fi[i-1])

print(fi[-1])