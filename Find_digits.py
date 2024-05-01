
def findDigits(n):
    # Write your code here
    digets=[]
    for num in str(n):
        digets.append(int(num))
    NoOfDiv=0
    for num in digets:
        if num ==0:
            continue
        if n%num==0 :
            NoOfDiv+=1
        
            
            
    return NoOfDiv
print(findDigits(10))