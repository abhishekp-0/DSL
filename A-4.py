def TransposeSparseMatrix(sp_r,sp) :
    rw=len(sp)
    cl=len(sp[0])
    nz_el=sp_r[0][2]
    print("Transpose of sparse matrix: ")
    trans_sp=[0]*(nz_el+1)
    ct=[0]*cl
    trans_sp[0]=[cl,rw,nz_el]
    for i in range(1,nz_el+1):
        ct[sp_r[i][1]]=ct[sp_r[i][1]]+1
    index=[1]*(cl+1)
    for i in range(1,cl+1):
        index[i]=index[i-1]+ct[i-1]
    for i in range(1,nz_el+1):
        x=index[sp_r[i][1]]
        trans_sp[x]=[sp_r[i][1],sp_r[i][0],sp_r[i][2]]
        index[sp_r[i][1]]=index[sp_r[i][1]]+1
    for i in range(0,nz_el+1):
        print(trans_sp[i])

def SimpleTranspose(sp_r):
    for i in range(sp_r[0][2]+1):
        temp=sp_r[i]
    rw=sp_r[0][0]
    cl=sp_r[0][1]
    trans_sp=[]
    nz_el=sp_r[0][2]
    sp_r=[]
    sp_r.append([cl,rw,nz_el])

    for i in range(cl):
        x=[]
        for j in range(rw):
            x.append(0)
        trans_sp.append(x)

    for i in range(cl):
        for j in range(rw):
            trans_sp[i][j]=sp[j][i]
            if(trans_sp[i][j]!=0):
                sp_r.append([i,j,trans_sp[i][j]])
    
    return sp_r

def AddSparse(sp1,sp2):
    r1=sp1[0][0]
    c1=sp1[0][1]
    n1=sp1[0][2]+1
    r2=sp2[0][0]
    c2=sp2[0][1]
    n2=sp2[0][2]+1
    sp3=[]
    sp3.append([r1,c1,0])
    if(r1!=r2 or c1!=c2):
        print("Given matrix cannot be added")
        return sp3

    i=1
    j=1
    while(i<n1 and j<n2):
        if(sp1[i][0]==sp2[j][0] and sp1[i][1]==sp2[j][1]):
            sp3.append([sp1[i][0],sp1[i][1],sp1[i][2]+sp2[j][2]])
            sp3[0][2]+=1
            i+=1
            j+=1
        elif(sp1[i][0]==sp2[j][0]):
            if(sp1[i][1]<sp2[j][1]):
                sp3.append(sp1[i])
                sp3.append(sp2[j])
            else:
                sp3.append(sp2[j])
                sp3.append(sp1[i])
            i+=1
            j+=1
            sp3[0][2]+=2

        else:
            if(sp1[i][0]<sp2[j][0]):
                sp3.append(sp1[i])
                i+=1
            else:
                sp3.append(sp2[j])
                j+=1
            sp3[0][2]+=1
            
    
    while(i<n1):
        sp3.append(sp1[i])
        i+=1
        sp3[0][2]+=1

    while(j<n2):
        sp3.append(sp2[j])
        j+=1
        sp3[0][2]+=1

    
    return sp3
            


    


rw=int(input("Enter no. of Rows : "))
cl=int(input("Enter no. of Columns : "))

sp=[]
nz_el=0
sp_r=[]
sp_r.append([rw,cl,0])

for i in range(rw):
    sp1=[]
    print("Enter elements of ",i+1,"th row")
    for j in  range(cl):
        x=int(input(""))
        if(x!=0):
            sp_r.append([i,j,x])
            nz_el=nz_el+1
        sp1.append(x)
    sp.append(sp1)

sp_r[0][2]=nz_el
print("sparse matrix is :")
for i in range(0,nz_el+1):
    print(sp_r[i])

sp2=[[3,3,4],[0,0,1],[1,1,1],[1,2,1],[2,1,1]]

print(AddSparse(sp_r,sp2))
TransposeSparseMatrix(sp_r,sp)
print(SimpleTranspose(sp,sp_r))

