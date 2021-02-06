import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))
A = sorted(A)

def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) // 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return True

for i in range(M):
    if binarySearch(A, X[i], 0, N-1):
        print(1)
    else:
        print(0)