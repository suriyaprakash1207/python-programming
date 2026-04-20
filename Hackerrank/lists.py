if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        # Split the input into command and arguments
        command_parts = input().split()
        cmd = command_parts[0]
        args = command_parts[1:]
        
        if cmd == "print":
            print(res)
        elif cmd == "insert":
            res.insert(int(args[0]), int(args[1]))
        elif cmd == "remove":
            res.remove(int(args[0]))
        elif cmd == "append":
            res.append(int(args[0]))
        elif cmd == "sort":
            res.sort()
        elif cmd == "pop":
            res.pop()
        elif cmd == "reverse":
            res.reverse()
