# Hashmap LEFT JOIN
 LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.
## Challenge
Write a function that LEFT JOINs two hashmaps into a single data structure.

- Write a function called left join
- Arguments: two hash maps
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
## Approach & Efficiency
I took the list as a data structure to store the ouput 
Time : O (N)
Space : O (N)

## Solution
![Hashmap_join_table](https://user-images.githubusercontent.com/61474974/172062018-1c43ba70-b2dc-4fa3-8833-f1c606d140e9.jpg)
