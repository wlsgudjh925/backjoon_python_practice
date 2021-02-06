N = int(input())
guitar = {}

for i in range(N):
    digit = 0
    serial = input()
    for j in serial:
        if j.isdigit():
            digit += int(j)
    guitar[serial] = digit

a = sorted(guitar.items(), key=lambda x : (len(x[0]),x[1],x[0]))

for i in a:
    print(i[0])