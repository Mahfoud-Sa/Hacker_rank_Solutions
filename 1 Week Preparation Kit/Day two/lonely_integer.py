#https://hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

def lonelyinteger(a):
    
    for i in a:
      if isUnique(i,a):
          return i 
            

def isUnique(num,arr):
    count=0
    for i in arr:
        if i ==num:
            count+=1
    if count==1:
        return True
    else:
        return False

print(lonelyinteger([1,2,3,4,3,2,1]))