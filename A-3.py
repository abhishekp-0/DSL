def displayMatrix(matrix):
    for i in matrix:
        print(i)

def add_Matrix(matrix1, matrix2):

    m1=len(matrix1)
    n1=len(matrix1[0])    
    m2=len(matrix2)
    n2=len(matrix2[0])  

    matrix3=[]

    if(m1!=m2 or n1!=n2):
        print("The given matrices cannot be added or subtracted!")
        return matrix3
    
    for i in range(m1):
        x=[]
        for j in range(n1):
            x.append(matrix1[i][j] + matrix2[i][j])
        matrix3.append(x)
    
    return matrix3

def sub_Matrix(matrix1, matrix2):
    m1=len(matrix1)
    n1=len(matrix1[0])    
    m2=len(matrix2)
    n2=len(matrix2[0])  

    matrix3=[]

    if(m1!=m2 or n1!=n2):
        print("The given matrices cannot be added or subtracted!")
        return matrix3
    

    for i in range(m1):
        x=[]
        for j in range(n1):
            x.append(matrix1[i][j] - matrix2[i][j])
        matrix3.append(x)
    
    return matrix3

def diagonal_Sum(matrix):
    m=len(matrix1)
    n=len(matrix1[0])  
    sum=0

    if(m!=n):
        print("Given matrix is not a square matrix!")
        sum=-1
        return sum

    for i in range(n):
        sum+=matrix[i][i]
    
    return sum

def upper_Triangle(matrix):
    m=len(matrix)
    n=len(matrix[0])

    sum=0
    for i in range(m):
        for j in range(i):
            if(matrix[i][j]!=0):
                return False
    
    return True

def multiply_Matrix(matrix1, matrix2):
    m1=len(matrix1)
    n1=len(matrix1[0])    
    m2=len(matrix2)
    n2=len(matrix2[0])

    matrix3=[]
    if(n1!=m2):
        print("Given matrices cannot be multiplied!")
        return matrix3
    
    for i in range(m1):
        x=[]
        for j in range(n2):
            x.append(0)
        matrix3.append(x)
   
    for i in range(m1):
        for j in range(n2):
            p=0
            for k in range(m2):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        
    
    return matrix3
    

def SaddlePoint(matrix):
    m=len(matrix)
    n=len(matrix[0])
    
    for i in range(m):
       
       
        min_row = matrix[i][0]
        col_ind = 0
        for j in range(1, m):
            if (min_row > matrix[i][j]):
                min_row = matrix[i][j]
                col_ind = j
 
        
        k = 0
        for k in range(n):
 
            
            if (min_row < matrix[k][col_ind]):
                break
            k += 1
 
        if (k == n):
            return min_row
 
    return 0

def transposeMatrix(matrix):
    m=len(matrix)
    n=len(matrix[0])

    result=[]
    for i in range(n):
        x=[]
        for j in range(m):
            x.append(0)
        result.append(x)

    for i in range(n):
        for j in range(m):
            result[j][i]=matrix[i][j]
    
    return result

        





m1=int(input("Enter no. of rows of first matrix: "))
n1=int(input("Enter no. of columns of first matrix: "))


matrix1=[]
matrix2=[]

for i in range(m1):
    x=[]
    for j in range(n1):
        print("Enter element of row ", i+1, " and column ", j+1, ": ")
        x.append(int(input()))
    matrix1.append(x)


m2=int(input("Enter no. of rows of second matrix: "))
n2=int(input("Enter no. of columns of second matrix: "))

for i in range(m2):
    x=[]
    for j in range(n2):
        print("Enter element of row ", i+1, " and column ", j+1, ": ")
        x.append(int(input()))
    matrix2.append(x)  

print("Matrix 1 : ")
displayMatrix(matrix1)
print("Matrix 2 : ")
displayMatrix(matrix2)


flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Diagonal Sum")
    print("5. Check for UpperTriangle")
    print("6. Saddle Point")
    print("7. Transpose")
    print("8. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 8) :"))

    if ch==1:
        print("Resultant matrix: ")
        displayMatrix(add_Matrix(matrix1, matrix2))
        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1

    elif ch==2:
        print("Resultant matrix: ")
        displayMatrix(sub_Matrix(matrix1, matrix2))
        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1

    elif ch==3:
        product=multiply_Matrix(matrix1,matrix2)
        if(len(product)==0):
            print("The given matrices cannot be multiplied")
        else:
            print("Product of the matrices : ")
            displayMatrix(product)
        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1
    elif ch==4:
        sum1=diagonal_Sum(matrix1)
        sum2=diagonal_Sum(matrix2)

        if(sum1!=-1):
            print("Diagonal sum of matrix 1 is ", end="")
            print(sum1)
        else:
            print("\n Given Matrix does not have a diagonal i.e it is not a square matrix")
        
        
        if(sum2!=-1):
            print("Diagonal sum of matrix 2 is ", end="")
            print(sum2)
        else:
            print("/n Given Matrix does not have a diagonal i.e it is not a square matrix")

        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1

    elif ch==5:
        if(upper_Triangle(matrix1)):
            print("Matrix 1 is an upper triangle")
        else:
            print("Matrix 1 is not an upper triangle")
        
        if(upper_Triangle(matrix2)):
            print("Matrix 2 is an upper triangle")
        else:
            print("Matrix 2 is not an upper triangle")

        a = input("Do you want to continue (yes/no) :")

        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1


    elif ch==6:
        s1=SaddlePoint(matrix1)
        s2=SaddlePoint(matrix2)

        if(s1==0):
            print("Matrix 1 does not have a saddle point")
        else:
            print("Value of Saddle point of Matrix 1 : " , s1)

        if(s2==0):
            print("Matrix 2 does not have a saddle point")
        else:
            print("Value of Saddle point of Matrix 2 : " , s2)
    
        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1

    elif ch==7:
        transpose1=transposeMatrix(matrix1)
        transpose2=transposeMatrix(matrix2)
        print("Transpose of matrix 1 : ") 
        displayMatrix(transpose1)
        print("Transpose of matrix 2 : ") 
        displayMatrix(transpose2)

        a = input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1

    elif ch==8:
        flag=0
        print("Thanks for using this program!")
        
    else:
        print("!!Wrong Choice!! ")
        a=input("Do you want to continue (yes/no) :")
        if a == "no":
            flag = 0
            print("Thanks for using this program!")
        else:
            flag=1


  