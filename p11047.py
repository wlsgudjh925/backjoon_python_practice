import sys

input = sys.stdin.readline

N, K = map(int, input().split())

L = []

for i in range(N):
    L.append(int(input()))

retval = 0

for i in L[::-1]:
    retval += K // i
    K = K % i

print(retval)