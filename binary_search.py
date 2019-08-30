import math

def binary_search(list,item):
    high = len(list)
    low = 0
    while low <= high:
        mid = math.floor((high+low)/2)

        guess = list[mid]

        if guess==item:
            print(mid)
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return print("No element was found")


mylist=[1,3,7,12,18,22,29,32,45,80]
binary_search(mylist,80)








