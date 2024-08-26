## Logik

Our friend Ardan wants to start a business, but he encountered a problem. Being an impeccable entrepreneur, he never thought that he would need computer science in this domain. Therefore, he is asking for help! A sequence of $N$ natural numbers is given. A subarray is valid if the sum of its elements is even. We define the value of a subarray as the AND sum (bitwise operation) of all numbers in the subarray. Ardan wants to find out the AND sum (bitwise operation) of the values of all valid subarrays. Calculate the value requested by Ardan to help him start his business. If there is no valid subarray, print -1.

## Task

The input file `logik.in` will contain on the first line a natural number $N$, and on the second line the $N$ natural numbers.

## Output data

The output file `logik.out` will print the AND sum (bitwise operation) of the values of all valid subarrays or -1 if there is no valid subarray.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$

$0 \leq$ Values in the array $\leq 10^9$

A subarray is formed by removing a prefix and/or a suffix of the initial sequence

For tests worth 20 points

$1 \leq N \leq 1\ 000$

For other tests worth 20 points all $N$ numbers are even

For other tests worth 60 points the initial constraints apply

## Example

`logik.in`
```
4
1 2 3 6
```

`logik.out`
```
2
```

## Explanation

All valid subarrays are: 
$[1, 2, 3]$ which has the value $3$
$[1, 2, 3, 6]$ which has the value $7$
$[2]$ which has the value $2$
$[6]$ which has the value $6$

$3 \text{ AND } 7 \text{ AND } 2 \text{ AND } 6 = 2$

For example, the subarray $[2, 3]$ is not valid because $2 + 3 = 5$ which is odd.