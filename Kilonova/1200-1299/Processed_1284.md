Ana discovered she has a true passion for palindromes.

A sequence of numbers is a palindrome if it reads the same from left to right and from right to left (the first number is equal to the last, the second to the second last, etc.).

She has an array with $N$ natural numbers and wants any subarray of odd length of the array to be a palindrome. To fulfill this wish, she can perform multiple operations on the array.

An operation consists of choosing an element from the array and incrementing or decrementing it by one. Of course, Ana wants to use a minimal number of operations for the resulting array to meet the property mentioned above (any subarray of odd length should be a palindrome).

# Task

Determine for Ana the minimum number of operations she needs to perform so that any subarray of odd length of the resulting array after performing the operations is a palindrome. Also, find out the number of distinct final arrays that can be obtained by performing this minimum number of operations.

# Input data

The input file `palind.in` will contain on the first line the number $T$, representing the number of input data sets to follow.

Next, the input data sets follow, each on two lines. The first line of a data set contains the number $N$, having the meaning from the statement. The next line contains the elements of the initial array, separated by a space.

# Output data

The output file `palind.out` will contain $T$ lines, with line $i$ containing two numbers, representing the answer for the $i$-th input data set.

The first number is the minimum number of operations, and the second the number of distinct final arrays that can be obtained by performing the minimum number of operations.

# Constraints and clarifications

* $1 \leq T \leq 20$
* $1 \leq N \leq 10\ 000$
* The elements of the array are natural numbers in the range $[1, 7\ 000]$
* A subarray of an array is a subsequence of numbers that appear in consecutive positions
* All tests used for correction will have $T = 20$

|#|Score|Constraints|
|:-:|:-:|:-:|
|1|$20\%$|$1 \leq N \leq 100$|
|2|$20\%$|The maximum value in any array is at most $500$ and $N \geq 101$|

# Example

`palind.in`
```
2
3
1 2 3
1
3
```

`palind.out`
```
2 3
0 1
```

# Explanation

For the first test, the three possible arrays are:
$1\ 2\ 1, 2\ 2\ 2$ and $3\ 2\ 3$.

For the second test, the only possible array is formed from the element $3$.