def Mergesort(arr):
    n = len(arr)
    # mid = []
    # left = []
    # right =[]
    if n >1:
        mid = int(n/2)
        left = arr[:mid]
        right = arr[mid:n]

        Mergesort(left)

        Mergesort(right)

        Merge(left,right,arr)


def Merge(left,right,arr):

    i = 0
    j = 0
    k = 0

    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i +=1
        else:
            arr[k] = right[j]
            j +=1

        k+=1

    if i ==len(left):
        for _ in range(j,len(right)):
            arr[k]= right[j]
            k+=1
            j +=1 
    else:
         for _ in range(i,len(left)):
            arr[k]= left[i]
            k+=1
            i +=1 

if __name__=="__main__":
    list1 = [5,2,1,7,12,0,4,8]
    Mergesort(list1)
    print(list1)
