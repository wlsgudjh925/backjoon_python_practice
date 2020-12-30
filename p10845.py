import sys
input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    command = input().rstrip()

    if command[0:4] == 'push':
        queue.append(command[5:])

    elif command[0:3] == 'pop':
        if queue == []:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)

    elif command[0:4] == 'size':
        print(len(queue))

    elif command[0:5] == 'empty':
        if queue == []:
            print(1)
        else:
            print(0)

    elif command[0:5] == 'front':
        if queue == []:
            print(-1)
        else:
            print(queue[0])

    elif command[0:4] == 'back':
        if queue == []:
            print(-1)
        else:
            print(queue[-1])