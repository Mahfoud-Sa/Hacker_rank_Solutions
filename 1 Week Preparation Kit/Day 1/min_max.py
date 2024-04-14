# hacker rink link:  https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
# min max problem
def miniMaxSum(arr):
    min=arr[0]
    max=arr[0]
    total=0
    for num in arr:
        total+=num
        if num > max:
            max=num
        if num < min:
            min=num
    print(total)
    print(min,max)
    print("{} {}".format(total-max,total -min))
    

miniMaxSum([7, 69 ,2 ,221, 8974])


