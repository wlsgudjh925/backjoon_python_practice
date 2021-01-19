n = 50000
a = [False, False] + [True]*(n-1) # 0과 1은 제외
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

primes_mul = []

for i in primes:
    for j in primes:
        if i != j and i*j <= 100001:
            primes_mul.append(i*j)

primes_mul.sort()

T = int(input())
for j in range(T):
    K = int(input())
    for i in primes_mul:
        if i >= K:
            print(i)
            break