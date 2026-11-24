def merge_the_tools(string, k):
    l = "\n".join("".join(dict.fromkeys(string[i:i+k])) for i in range(0 ,len(string) ,k))
    print(l)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)