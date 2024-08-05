def addPoly(p1,p2):
    n1=len(p1)
    n2=len(p2)
    p1=p1[::-1]
    p2=p2[::-1]
    if(n1>=n2):
        p3=p1
        for i in range(n2-1,-1,-1):
            p3[i]+=p2[i]
    else:
        p3=p2
        for i in range(n1-1,-1,-1):
            p3[i]+=p1[i]
    return p3[::-1]

def displayPoly(p1):
    n=len(p1)
    power=n-1
    for i in p1:
        
        print(i,"x^",power,"+",end="",sep="")
        power-=1

p1=[2,0,4,0,2,4]
p2=[3,7,3,1]

displayPoly(addPoly(p1,p2))

