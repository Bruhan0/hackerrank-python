def split_join(s):
    return "-".join(s.split())
if __name__ == "__main__" :
    s = input()
    result = split_join(s)
    print(result)