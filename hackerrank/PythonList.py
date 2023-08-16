if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        commands = input().split()
        command = commands[0]
        if command == 'insert':
            pos = int(commands[1])
            val = int(commands[2])
            list.insert(pos, val)
        elif command == 'print':
            print(list)
        elif command == 'append':
            val = int(commands[1])
            list.append(val)
        elif command == 'remove':
            val = int(commands[1])
            list.remove(val)
        elif command == 'sort':
            list.sort()
        elif command == 'pop':
            list.pop()
        elif command == 'reverse':
            list = list[::-1]
    