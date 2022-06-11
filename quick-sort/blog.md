# Quick Sort
it takes in an array and then It picks an element as pivot and partitions the given array around the picked pivot and return that array sorted from pivate by dividiing the aray usng (partition) function

given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.

* Partition the array by setting the position of the pivot value.

* create a variable to track the largest index of numbers lower than the defined pivot.

* place the value of the pivot location in the middle.

* all numbers smaller than the pivot are on the left, larger on the right.

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
trace:
![quick1](https://user-images.githubusercontent.com/61474974/173194516-1942c667-d01b-486f-97a9-f203cb037956.jpg)


On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.

## summary
Step 1 − Make any element as pivot

Step 2 − Partition the array on the basis of pivot

Step 3 − Apply quick sort on left partition recursively

Step 4 − Apply quick sort on right partition recursively

## Big O
space:
The average case space used will be of the order O(n*log n).

Time:
The worst case Time used will be O(n^2) . 
The average case space used will be of the order O(n*log n).
