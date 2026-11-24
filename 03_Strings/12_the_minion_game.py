def minion_game(s):
    l = k = 0
    for i in range(len(s)):
        if s[i] in "AEIOU": k += len(s)-i
        else : l += len(s)-i
    if k > l : print("Kevin", k)
    elif l > k : print("Stuart",l)
    else : print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)