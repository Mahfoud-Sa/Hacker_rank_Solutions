
def diagonalDifference(arr):
    r_sum=0
    l_sum=0
    lenght=len(arr)
    

    for i in range(lenght):
        for j in range(lenght):
            if i==j:
                r_sum+=arr[i][j]
    
    for i in range(lenght):
        
        l_sum+=arr[i][lenght-(i+1)]
    
    
    return (abs( r_sum-l_sum))
    # Write your code here

diagonalDifference([[1,2,3],[4,5,6],[9,8,9]])