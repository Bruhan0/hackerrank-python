def Lists_methods(l, methods):
    for i in methods:
        case = i.split(" ")
        match case[0]:
            case "insert":
                l.insert(int(case[1]), int(case[2]))
            case "print":
                print(l)
            case "remove":
                l.remove(int(case[1]))
            case "append":
                l.append(int(case[1]))
            case "sort":
                l.sort()
            case "pop":
                l.pop()
            case "reverse":
                l.reverse()
if __name__ == '__main__':
    N = int(input())
    methods = [input() for i in range(N)]
    l = []
    Lists_methods(l, methods)
        
    