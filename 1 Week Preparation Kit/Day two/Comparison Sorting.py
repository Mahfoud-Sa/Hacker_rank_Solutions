def countingSort(arr):
    # Write your code here
    index_list=[0]*100
    for item in arr:
        index_list[item]+=1
    return index_list