Ionel has a new problem to solve. He needs to construct an array of $N$ natural numbers. The numbers in the array can have only one-digit **prime** numbers as their prime divisors. After constructing the array, Ionel noticed that there are subarrays in the array for which the product of the elements is the cube of a natural number.

# Task

Ionel wants to determine the number of subarrays in the constructed array whose product of elements equals the cube of a natural number.

# Input data

The input file `cub.in` will contain on the first line the natural number $N$, and on the next line will contain $N$ natural numbers separated by a space, the elements of the array constructed by Ionel.

# Output data

The output file `cub.out` will contain on the first line a natural number representing the number of subarrays in the constructed array whose product of elements equals the cube of a natural number.

# Constraints and clarifications

* $N$ and the elements of the array are natural numbers in the interval $[2,10^6].$
* By subarray of an array, we understand a sequence of one or more terms from the array found on consecutive positions.
* For tests worth $20$ points, $N \leq 1 \\ 000.$
* For tests worth $40$ points, $N \leq 10 \\ 000.$

# Example

`cub.in`

```
8
15 3 5 15 7 63 21 125
```

`cub.out`

```
6
```

## Explanation

There are $6$ subarrays in the array with the product of the elements equal to a value that is the cube of a natural number:

$$
\mathbf{1)} \ \ 15,\ 3, \ 5, \ 15; \\
\mathbf{2)} \ \ 7, \ 63, \ 21; \\
\mathbf{3)} \ \ 125; \\
\mathbf{4)} \ \ 15, \ 3, \ 5, \ 15, \ 7, \ 63, \ 21; \\
\mathbf{5)} \ \ 7, \ 63, \ 21, \ 125; \\
\mathbf{6)} \ \ 15, \ 3, \ 5, \ 15, \ 7, \ 63, \ 21 \ 125;
$$