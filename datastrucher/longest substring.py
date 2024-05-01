string=input("enter your string: ")
maxSubStr=''
for i in range(len(string)):
    temp=''
    for char in string[i:]:
        if char in temp:
            break
        else:temp+=char
    if len(temp)>len(maxSubStr):
        maxSubStr=temp
    
print(maxSubStr)