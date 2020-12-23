n = int(input())
count = 1
new = (n%10)*10 + (n//10+n%10)%10
while new != n:
    new = (new%10)*10 + (new//10+new%10)%10
    count = count + 1
print(count)