def flippingMatrix(matrix):
    _len=len(matrix)
    max_r=matrix[0]
    max_r_i=0
    for i in range(_len):
        if max(matrix[i])>max_r:
            max_r=max(matrix[i])
            max_r_i=i

    print(max_r)
            
    sum=0
    
    for i in range(_len//2):
        for j in range(_len//2):
            sum+=matrix[i][j]
            
    return sum
matrix=[
    [112,42,83,119],
    [56,125,56,49],
    [15,78,101,43],
    [62,98,114,108],
]

flippingMatrix(matrix)