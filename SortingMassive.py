def findsmallest(massive):
    smallestelement  =massive[0]
    smallestelementIndex=0
    for index in range(0,len(massive)):

        if massive[index]<smallestelement:
            smallestelement=massive[index]
            smallestelementIndex=index

    return smallestelementIndex
def Sortmassive(arr):
    newarr=[]
    for i in range(0,len(arr)):
        smallest=findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(Sortmassive([5,90,7,9,8,3,49,1669,23]))

