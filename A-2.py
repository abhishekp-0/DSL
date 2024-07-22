def union(x,y):
    r=x.copy()

    for i in y:
        if(i not in r ):
            r.append(i)
    
    return r

def intersection(x,y):
    r=[]

    for i in x:
        if(i in y):
            r.append(i)
    
    return r

def subtract(x,y):
    r=[]

    for i in x:
        if(i not in y):
            r.append(i)

    return r

n=int(input("Enter Total no. of Students:"))
a=[]
b=[]
c=[]
n_a=int(input("Enter Number of students who play cricket:"))
print("Enter Roll no.s of students who play Cricket:")
for i in range(n_a):
    x=int(input())
    a.append(x)

n_b=int(input("Enter Number of students who play Badminton:"))
print("Enter Roll no.s of students who play Badminton:")
for i in range(n_b):
    x=int(input())
    b.append(x)

n_c=int(input("Enter Number of students who play Football:"))
print("Enter Roll no.s of students who play Football:")
for i in range(n_c):
    x=int(input())
    c.append(x)

print("The required list are:")
print("Cricket:",a)
print("Badminton:",b)
print("Football:",c)

#students who play both cricket and badminton
print("students who play both cricket and badminton: ",intersection(a,b))

print("students who play either cricket or badminton but not both: ", subtract(union(a,b),intersection(a,b)))

print("number of students who play neither cricket nor badminton: ",n-len(union(a,b)))

print("number of students who play  cricket and football but not badminton: ",len(union(a,b))-len(c))

print("students who do not play any game: ",n-len(union(c,union(a,b))))

print("students who play at least one game: ",union(c,union(a,b)))

print("students who play all the games: ",intersection(c,intersection(a,b)))


