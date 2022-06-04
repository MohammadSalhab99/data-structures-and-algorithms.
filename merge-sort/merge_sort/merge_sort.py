def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(lefthalf, righthalf, arr)

    return arr


def merge(lefthalf, righthalf, arr):
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            arr[k] = lefthalf[i]
            i = i+1
        else:
            arr[k] = righthalf[j]
            j = j+1
        k = k+1

    if i < len(lefthalf):
        arr[k] = lefthalf[i]
        i = i+1
        k = k+1

    elif j < len(righthalf):
        arr[k] = righthalf[j]
        j = j+1
        k = k+1