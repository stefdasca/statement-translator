In a sequence of natural numbers, we call a sequence **dsecv** a series of consecutive positions $a_i$, $a_{i+1}$, $a_{i+2}$, $a_{i+3}$, $\\dots$, $a_j$ with $i \\leq j$ if any two adjacent numbers in the sequence $(a_i, a_{i+1})$ have the property that the number of divisors of $a_i \\leq$ the number of divisors of $a_{i+1}$. The number of elements in the sequence represents the length of the sequence.  
For example, in the array $13$, $20$, $24$, $3$, $12$, $100$, $2$, $17$, $18$ there are $3$ **dsecv** sequences of length $3$: $(13, 20, 24)$; $(3, 12, 100)$ and $(2, 17, 18)$.

# Task

Given the natural number $C$ representing the task number, a natural number $n$, and then an array of $n$ non-zero natural numbers with a maximum of $9$ digits each, write a program that solves the following tasks: 
1. If $C=1$, among all values in the array that have the maximum number of divisors, determine the minimum value and the maximum value. 
2. If $C=2$, determine the number of **dsecv** sequences of maximum length in the array and the maximum length of such a sequence.

# Input data

The input file `dsecv.in` contains on the first line the number $C$ representing the task ($1$ or $2$) and the natural number $n$, and on the second line an array of $n$ natural numbers, the values on the same line being separated by spaces.

# Output data

If the task $C=1$, then on the first line of the output file `dsecv.out`, determine among all the values in the array that have the maximum number of divisors, the minimum value, and the maximum value; these should be written in ascending order, separated by a space.

If the task $C=2$, then on the first line of the output file `dsecv.out` write, separated by a space, two natural numbers representing the number of **dsecv** sequences of maximum length in the array and the maximum length of such a sequence.

# Constraints and clarifications

* $1 \\leq n \\leq 10^4$;
* $1 \\leq C \\leq 2$;
* $1 \\leq a_i \\leq 10^9$;
* For $40$ points the task will be $C=1$;
* For $50$ points the task will be $C=2$;
* $10$ points are awarded by default.

# Example 1

`dsecv.in`
```
1 10 
13 20 24 3 12 100 120 2 432 18
```

`dsecv.out`
```
432 432
```

## Explanation

The number $432$ has the most divisors (it is both minimum and maximum).

# Example 2

`dsecv.in`
```
2 10 
13 20 24 3 12 100 120 2 432 18
```

`dsecv.out`
```
1 4
```

## Explanation

The array contains $1$ **dsecv** sequence of length $4$. $\\text{dsecv} = (3, 12, 100, 120)$.