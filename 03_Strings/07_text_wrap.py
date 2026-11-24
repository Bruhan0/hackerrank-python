def wrap(string, max_width):
    res =""
    ch_length =""
    for i in string:
        ch_length += i
        if len(ch_length) == max_width :
            res += ch_length + "\n"
            ch_length = ''
    res += ch_length + "\n"
    return result[:-1]

# Or

    return "\n".join([string[i:i+max_width] for i in range(0,len(string),max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)