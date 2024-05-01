
def hDiv(n):
    hDiv=0
    for i in range(n-1,0,-1):
        if n%i==0:
            hDiv=i
            break
    return hDiv



print(hDiv(3))


