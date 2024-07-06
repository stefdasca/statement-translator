Gigel participates in the informatics olympiad and faces the following challenge: he has an array of $N$ numbers and wants to find a subarray with a length between $S$ and $D$, such that the sum of the elements in this subarray is maximal. Moreover, Gigel has decided that this sum must also be a power of $K$.
The goal is to write a program that determines the subarray with a length between $S$ and $D$ that has the highest sum and is a power of $K$.
If multiple subarrays have the same maximum sum but do not have the same length, the starting index of the shortest subarray is displayed. If multiple subarrays have the same maximum sum and the same minimal length, the starting index of the last found subarray is displayed.

# Input data

The input file `sub2max.in` contains on the first line four integers, $N, S, D$, and $K$, separated by space. On the next line, there will be $N$ numbers, the elements of the array.

# Output data

The output file `sub2max.out` will contain on the first line two numbers: the maximum sum that is a power of $K$ and the starting index of the subarray corresponding to this sum.

# Constraints and clarifications

* $1 \leq N \leq 10^4$
* $1 \leq S \leq D \leq N$
* $1 \leq K \leq 130$
* The elements of the array are numbers in the interval $[-10^7, 10^7]$
* If there is no solution, $-1$ will be printed for both the value of the maximum sum and the starting index.
* The indices of the array are numbered starting from $1$.
* For tests worth $30$ points, $N \leq 10^3$
* For other tests worth $70$ points, there are no additional restrictions.

# Example 1

`sub2max.in`
```
5 1 3 3
3 12 15 12 15
```

`sub2max.out`
```
27 4
```

## Explanation

We have an array of $5$ numbers and need to find a subarray with a length between $1$ and $3$ elements, such that the sum of the elements is maximal and is a power of $3$. The highest sum that is a power of $3$ and meets the subarray length conditions is $27$, and this is obtained for the subarrays of length $2$ starting from the indices $2, 3$, and $4$. Since in this case all three subarrays have the same minimal length $2$, the starting index of the last found subarray is considered, namely $4$.

# Example 2

`sub2max.in`
```
7 2 4 2
1 2 4 8 16 32 64
```

`sub2max.out`
```
-1 -1
```

## Explanation

We have an array of $7$ numbers and need to find a subarray with a length between $2$ and $4$ elements, such that the sum of the elements is maximal and is a power of $2$. In the given array, there is no subarray such that the sum of the elements is maximal and is a power of $2$.

# Example 3

`sub2max.in`
```
10 2 5 2
-1 3 -2 7 4 1 6 3 2 -5
```

`sub2max.out`
```
16 5
```

## Explanation

We have an array of $10$ numbers and need to find a subarray with a length between $2$ and $5$ elements, such that the sum of the elements is maximal and is a power of $2$. The highest sum that is a power of $2$ and meets the subarray length conditions is $16$, and this is obtained for the subarray starting from index $3$ and has a length of $16 \ ([-2, 7, 4, 1, 6])$ and for the subarray starting from index $5$ and has a length of $16 \ ([4, 1, 6, 3, 2])$. Since in this case both subarrays have the same minimal length $2$, the starting index of the last found subarray is considered, namely $5$.