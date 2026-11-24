def solve(s):    
    #return " ".join([i.capitalize() for i in  s.split(" ")]) # the problem with this is it works but for s = "hello WORLD" , it gives Hello World..... So i came up with another idea  
    return " ".join([i[0].upper()+i[1:] if i else "" for i in s.split(" ") ]) # And it's working , Lol
