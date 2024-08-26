# Subsir100

Andreea received a sequence of $N$ natural numbers from her friend Ioana. Since Ioana likes interesting subarrays, she asked Andreea to count how many distinct interesting subarrays the sequence contains. A subarray is interesting if any two numbers in the subarray are different from each other. Because the number of interesting subarrays can be large, Andreea asks you to find only the remainder of this number when divided by $1000003$.

## Input data

The input file `subsir100.in` contains a natural number $N$ on the first line, having the meaning described in the statement. On the next line, there are $N$ natural numbers, separated by a single space, representing the sequence of numbers.

## Output data

The output file `subsir100.out` will contain the total number of interesting subarrays, modulo $1000003$.

## Constraints and clarifications

$1 \leq N \leq 100000$

The numbers in the sequence are natural numbers smaller than $2000000000$.

Considering that the given sequence is $A=(a_1, a_2, \dots, a_N)$, a subarray of $A$ is a sequence $B=(a_{i_1}, a_{i_2}, \dots, a_{i_K})$ with the property $1 \leq i_1 < i_2 < \dots < i_K \leq N$.

Two subarrays $B=(b_{i_1}, b_{i_2}, \dots, b_{i_K})$ and $C=(c_{j_1}, c_{j_2}, \dots, c_{j_P})$ are distinct if $K$ is different from $P$ or there exists $q$ such that $i_q$ is different from $j_q$.

## Example

`subsir100.in`

```
3 
1 1 2 
```

`subsir100.out`

```
5 
```

## Explanation

The 5 interesting subarrays are marked in bold: $1, 1, 2$, $1, 1, 2$, $1, 1, 2$, $1, 1, 2$, and $1, 1, 2$.