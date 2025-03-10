Here's the translated competitive programming problem statement with the specified instructions applied:

Given the natural number $n$ and an array $a$ consisting of $n$ natural numbers. We define a special subarray as a subarray of the form $a_i, a_{i+1},\dots, a_j$ with the property that $a_i = a_j$. We call the sum of a subarray $a_i,a_{i+1},\dots, a_j$, the sum of all the values in the subarray.

# Task

Given the number $n$ and the array $a$ with $n$ natural numbers, determine the sum of the sums of all the special subarrays in the array.

# Input data

The file `secvente.in` will contain on the first line the natural number $n$, and on the next line $n$ natural numbers separated by spaces.

# Output data

The file `secvente.out` will contain on the first line a natural number representing the sum of the sums of all the special subarrays from the array read from the input file. Since this number can be very large, it will be displayed modulo $10^9+7$.

# Constraints and clarifications

* $1 \le n \le 2 \cdot 10^5$;
* $1 \le a_i \le 2 \cdot 10^5$.

| # | Points | Constraints                |
|---|--------|----------------------------|
| 1 | 20     | $1 \le n \le 2 \cdot 10^2$ |
| 2 | 20     | $1 \le n \le 2 \cdot 10^3$ |
| 3 | 60     | No other constraints exist. |

# Example 1

`secvente.in`
```
5 
1 2 1 2 1
```

`secvente.out`
```
27 
```

## Explanation

The special subarrays are: $[1, 1], [1, 3], [1, 5], [2, 2], [2, 4], [3, 3], [3, 5], [4, 4], [5, 5]$

# Example 2

`secvente.in`
```
18 
5 185 19582 5 536 185 462 536 19582 5 19582 185 462 19582 536 5 462 19582 
```

`secvente.out`
```
1338362 
