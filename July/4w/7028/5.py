def Rev(x): 
    if type(x)==int:
        x=str(x)
    rev_x=x[::-1]
    
    return int(rev_x)

#Rev(Rev(X) + Rev(Y))

a,b=input().split()
#print((Rev(a) + Rev(b)))
print(Rev(Rev(a) + Rev(b)))