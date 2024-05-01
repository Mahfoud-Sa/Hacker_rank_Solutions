a=[2,4]
b=[24,36]

#get factors
print('factor')
factor=0
for num in range(2,0,-1):
    if 2 % num==0:
       factor=num
       break
for num in range(4,0,-1):
    if 4%num and num ==factor:
        break

print(factor)