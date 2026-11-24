def check(n):
    if n%2 or 6<= n <=20 : print("Weird") #simply, Odd or even, and lies in b/w 6 to 20 
    else: print("Not Weird")
if __name__ == '__main__':
    n = int(input().strip())
    check(n)