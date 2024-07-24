def linearSearch(l,n):
    count = 0
    for i in range(len(l)):
        count+=1
        if(l[i]==n):
            print("key found after ", count , " comparisons at position ", i+1, " with Linear Search")
            return i
    print("Key not found with Linear Search!! Comparisions done : " ,count)
    return -1    

def sentinelSearch(a,key):
    count = 0
    i=0
    a.append(key)
    while(key!=a[i]):
        count+=1
        i+=1
    a.pop()
    if(i<len(a)):
        print("key found after ", count , " comparisons at position ", i+1, " with Sentinel Search")
        return i
    else:
        print("Key not found with Sentinel Search!! Comparisions done : " ,count)
        return -1 
    
def binarySearch(key,a,f,l):
    count=0
    a.sort()
    while(f<=l):
        count+=1
        mid=int((f+l)/2)
        if(key==a[mid]):
            print("key found after ", count , " comparisons at position ", mid+1 , " with Binary Search")
            return mid+1
        elif(a[mid]<key) :
            f=mid+1
        elif(a[mid]>key):
            l=mid-1
    print("Key not found with Binary Search!! Comparisions done : " ,count)
    return -1

a=[]
n=int(input("Enter no.of elements in array"))
for i in range(n):
    x=int(input("Enter element"))
    a.append(x)        

flag=1
while (flag==1):
    
    key=int(input("Enter element to be searched : "))
    linearSearch(a,key)
    binarySearch(key,a,0,len(a)-1)
    sentinelSearch(a,key)
    r=input("Do you want to continue (y/n) : ")
    if(r=="y"):
        flag=1
    else:
        flag=0



 
