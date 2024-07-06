```markdown
A number $n$ is read from the keyboard and then $n$ natural numbers. We define a sequence as a group of elements on consecutive positions in the read array. We define a tri-subarray as a subarray that starts with an odd element, ends with an odd element, and contains exactly one other odd element in between. Thus, each tri-subarray includes two maximal subarrays formed only of even elements (each of these two may be empty). The imbalance of a tri-subarray is calculated as follows: determine the sum of elements in the subarray on the left formed only of even elements, the sum of elements in the subarray on the right formed only of even elements, and then the absolute difference between the two values (i.e., subtract the smaller one from the larger one). If any of the two subarrays of even elements is empty, it is considered to have a sum of $0$. This difference represents the imbalance of the tri-subarray.

# Task

Determine a tri-subarray with minimum imbalance. If there are multiple such tri-subarrays, determine the one that starts at the greatest possible position.

# Input data

The input file `tri.in` contains on the first line a natural number $n$ representing the number of elements in the given array. The second line contains $n$ natural numbers representing the elements of the array, in increasing order of positions, numbered starting with $1$. In the input tests, $n$ is given on one line, and the elements of the array on the next line separated by a space.

# Output data

The output file `tri.out` will contain on the first line two natural numbers between $1$ and $n$ (inclusive), separated by a space, representing the starting and ending positions of the determined tri-subarray.

# Constraints and clarifications

* $3 \leq n \leq 100\ 000$
* The value of an element can be from $0$ to $1\ 000\ 000\ 000$.
* The array contains at least $3$ odd elements.

# Example 1

`tri.in`
```
16
2 3 8 7 4 2 5 10 7 9 8 11 8 2 13 6
```

`tri.out`
```
10 15
```

## Explanation

We have $5$ tri-subarrays:
- $(3, 8, 7, 4, 2, 5)$, with imbalance $2$;
- $(7, 4, 2, 5, 10, 7)$, with imbalance $4$;
- $(5, 10, 7, 9)$, with imbalance $10$;
- $(7, 9, 8, 11)$, with imbalance $8$;
- $(9, 8, 11, 8, 2, 13)$, with imbalance $2$.
```