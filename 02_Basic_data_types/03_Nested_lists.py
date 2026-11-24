def second_lowest(l):
    d = {}
    for name ,score in l:
        if score in d :
            d[score].append(name)
        else: d[score] = [name]
    for i in sorted(d[sorted(d)[1]]):
        print(i)
        
if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    second_lowest(l)
        
# First, the main block runs , it reads n and runs n times...
#l.append([name,score]) this makes, [name,score] pair's as a list
#i first created a empty dictionary to make key as score and value as name ,
#so that i can sort the dictionary acc to score and sorting values alphabatically in the sorted dictionary 
