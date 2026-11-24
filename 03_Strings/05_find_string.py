def count_substring(string, sub_string):   
    s = len(sub_string)
    return sum(1 for ch in range(len(string)-s+1) if string[ch:s+ch] == sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)