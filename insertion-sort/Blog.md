# Insertion Sort
Insertion sort is the sorting mechanism where the sorted array is built having one item at a time. The array elements are compared with each other sequentially and then arranged simultaneously in some particular order.
 
### Psuedo Code

    InsertionSort(int[] arr)

        FOR i = 1 to arr.length

        int j <-- i - 1
        int temp <-- arr[i]

        WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1

        arr[j + 1] <-- temp



Steps:
Starting Insertion Sort.

![Capture](https://user-images.githubusercontent.com/61474974/170733228-eb546eea-ae60-4731-b526-c67f87b161fd.PNG)

Steps:

Highlighted green records to the left are always sorted. We begin with the record in position 0 in the sorted portion, and we will be moving the record in position 1 (in blue) to the left until it is sorted.
Steps:
Processing record in position 1
Steps:
Move the blue record to the left until it reaches the correct position.

![2](https://user-images.githubusercontent.com/61474974/170733342-832d336f-3278-4ed5-8db0-94a0b87d4c4f.PNG)

Steps:
Swap.

![3](https://user-images.githubusercontent.com/61474974/170733355-5217e217-f1f8-41ad-afd7-f13540d0df27.PNG)

Steps:
Processing record in position 2

Steps:
Move the blue record to the left until it reaches the correct position.

![4](https://user-images.githubusercontent.com/61474974/170733369-2bcbdbe7-832c-4778-99db-e395fe917bdd.PNG)

Steps:
Processing record in position 3

Steps:
Move the blue record to the left until it reaches the correct position.

![5](https://user-images.githubusercontent.com/61474974/170733375-d142a3d0-6ee4-4643-bf2f-e7555148f797.PNG)

Steps:
Processing record in position 4

Steps:
Move the blue record to the left until it reaches the correct position.

![6](https://user-images.githubusercontent.com/61474974/170733380-3dfc5eae-4667-4ef2-8934-d9d34c083ad8.PNG)

Steps:
Swap.

![7](https://user-images.githubusercontent.com/61474974/170733389-ffb7e702-3a25-46f3-8ad7-ef302ff95468.PNG)

Steps:
Move the blue record to the left until it reaches the correct position.

![8](https://user-images.githubusercontent.com/61474974/170733422-613ad422-0d50-41a0-8581-45ff63383ec7.PNG)

Steps:
Move the blue record to the left until it reaches the correct position.

![9](https://user-images.githubusercontent.com/61474974/170733436-db7fd9d1-7e31-4413-b185-7e0f62155220.PNG)

Steps:
Swap.

![10](https://user-images.githubusercontent.com/61474974/170733448-6647ad66-680d-490a-b448-f880484e1ffc.PNG)


Steps:
Swap.

![11](https://user-images.githubusercontent.com/61474974/170733465-73f5dc69-7be3-40fc-bfcc-474ac56fc707.PNG)

Steps:
Swap.

![12](https://user-images.githubusercontent.com/61474974/170733472-7ed594bc-9633-450b-98e8-0631c26e691a.PNG)

Steps:
Done sorting!

![13](https://user-images.githubusercontent.com/61474974/170733479-7fda2a34-3786-42bb-9670-c0cb07635039.PNG)

- ## Time: O(n^2)

    The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
- ## Space: O(1)

    No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).