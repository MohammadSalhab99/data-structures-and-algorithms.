# Merge-Sort

Merge-sort is one the famous algorithms for sorting. It uses the divide and conqoure techniqe for sorthing the list.

![Merge-sort](https://user-images.githubusercontent.com/61474974/173191351-2ad7bf4c-ac66-4a31-8999-75e159d3482c.jpg)


## Pseudo code
    
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left

## Going through the algorithm

Now if we have this list and we want to sort the list using the merge sort 
how the alogrithm will work
![1](https://user-images.githubusercontent.com/61474974/173191558-1a0338c1-6790-4b1f-9e2c-08f6dd4169e6.PNG)

First thing will happen is that the algorithm will divide the arr into two parts until the list has only one element 
The left part will look like this :

![2](https://user-images.githubusercontent.com/61474974/173191545-e1170685-26fe-46e1-9ee6-4d311de309a9.PNG)

And The right part will look like this :

![3](https://user-images.githubusercontent.com/61474974/173191546-66ef80b7-55c1-4794-877e-4190b750b218.PNG)

The For Each part the algorithm will divide into two parts.


![4](https://user-images.githubusercontent.com/61474974/173191547-6e57c649-66f6-4dc4-81da-fb549f45bb9e.PNG)

![5](https://user-images.githubusercontent.com/61474974/173191549-c2457b71-0714-4e31-a512-559b8d728924.PNG)


Now if any of the divided parts has only one element in it, it will not divide it and we will keep dividing the other part

![6](https://user-images.githubusercontent.com/61474974/173191550-9bade2f0-cbef-4c5d-8855-517dd79745b5.PNG)

![7](https://user-images.githubusercontent.com/61474974/173191552-95ac748d-a910-49d6-aa90-50f5584e8780.PNG)

Now we will define i as the index of the left array and the j for the right and the k is the index of the arr
and we will check if left[i]<= right[j] we will put the arr[k] = left[i]
else we will put the right element in the first 

![8](https://user-images.githubusercontent.com/61474974/173191553-384ecba0-9178-49f7-8d39-3c7cca327005.PNG)

![10](https://user-images.githubusercontent.com/61474974/173191555-aec4306b-62c5-45fa-9127-ce1241db86d6.PNG)

After we finsh we will check if the i is = length of the left  we will set remaining entries in arr to remaining values in right
otherwise  set remaining entries in arr to remaining values in right.

![9](https://user-images.githubusercontent.com/61474974/173191554-1ce7e7a6-0b7a-4462-bb23-de93b026c068.PNG)

![11](https://user-images.githubusercontent.com/61474974/173191556-559de12f-9602-439d-88c9-87ca9bd2b15a.PNG)

Finally the list will be sorted :

![12](https://user-images.githubusercontent.com/61474974/173191557-0ae9bf99-d956-497b-a8f7-801605633430.PNG)



_______________
## Big O complexity of this Algorithm


Time:  O(n*Log n) in all the 3 cases (worst, average and best)

Space : O(1)



