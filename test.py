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

print(transposeMatrix([[1,2,3],[4,5,6],[7,8,9]]))
