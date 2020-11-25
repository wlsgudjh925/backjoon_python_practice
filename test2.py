from random import*

randimg = range(1, 151)
randimg = list(map(str, randimg))
shuffle(randimg)

for i in range(10):
    f = open(randimg[i]+".txt", 'r', encoding='UTF8')
    while True:
        line = f.readline()
        print(line)
        if not line: break
    f.close()
