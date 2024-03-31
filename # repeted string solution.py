# Plus Minus solution
# problem link in hackerrank
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

def plusMinus(arr):
    # Write your code here
    NoPos=0
    NoNeg=0
    NoZe=0
    for num in arr:
        if num < 0:
            NoNeg+=1
        elif num > 0:
            NoPos+=1
        else:
            NoZe+=1
    
    

    print(NoPos/len(arr))
    print(NoNeg/len(arr))
    print(NoPos/len(arr))

plusMinus([-4, 3, -9, 0, 4, 1])