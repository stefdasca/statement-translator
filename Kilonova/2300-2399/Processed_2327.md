A natural number is called a kpower if it is a power of the natural number $k$. A kpower sequence is a subarray of kpower numbers that appear on consecutive positions in an array.

# Task

Given a natural number $k$ and an array of $n$ natural numbers, write a program that solves the following tasks:

1. Determine the largest kpower number among the given $n$ numbers.
2. Determine the maximum length of a kpower sequence.
3. Determine the largest sum that can be obtained by summing the numbers in a kpower sequence of maximum length.

# Input data

The input file `kpower.in` contains the following:
- The first line contains the number $C$ representing the task ($1$, $2$, or $3$).
- The second line contains the numbers $k$ and $n$.
- The third line contains an array of $n$ numbers, with the numbers on the same line separated by a space.

# Output data

If the task is $C=1$, then the first line of the output file `kpower.out` will contain the largest kpower number found.
If the task is $C=2$, then the first line of the output file `kpower.out` will contain the maximum length of a kpower sequence.
If the task is $C=3$, then the first line of the output file `kpower.out` will contain the largest sum of a kpower sequence of maximum length.

# Constraints and clarifications

* $0 < k \leq 9$
* $1 \leq n \leq 10^{6}$
* The $n$ numbers read are from the interval $[0,10^{12}]$.
* For all test cases, there is at least one kpower number among the $n$ numbers.
* For test cases worth $20$ points, $C=1$.
* For test cases worth $30$ points, $C=2$.
* For test cases worth $40$ points, $C=3$.

# Example 1

`kpower.in`
```
1
3 19
1 27 9 17 21 3 1 27 3 9 81 78 56 1 3 9 1 81 9
```

`kpower.out`
```
81
```

## Explanation

$k$ is $3$, and the largest number in the array that is a power of $3$ is $81$.

# Example 2

`kpower.in`
```
2
3 19
1 27 9 17 21 3 1 27 3 9 81 78 56 1 3 9 1 81 9
```

`kpower.out`
```
6
```

## Explanation

The kpower sequences in the array are $(1, 27, 9)$, $(3, 1, 27, 3, 9, 81)$, and $(1, 3, 9, 1, 81, 9)$. The maximum length of a kpower sequence is $6$.

# Example 3

`kpower.in`
```
3
3 19
1 27 9 17 21 3 1 27 3 9 81 78 56 1 3 9 1 81 9
```

`kpower.out`
```
124
```

## Explanation

Among the two kpower sequences of maximum length, the first one has the maximum sum of numbers: $3+1+27+3+9+81=124$.