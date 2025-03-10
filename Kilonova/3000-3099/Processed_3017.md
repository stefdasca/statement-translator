Consider an array consisting of $n$ natural numbers. The following processing is done on the numbers in the array: each value is replaced with its largest prime divisor. In the new array, sequences of numbers are formed that start and end with the same value, called non-uniform sequences.

# Task

Given the natural numbers $n$ and $c$, and an array of $n$ natural numbers, the following tasks need to be solved: 
1. If $c=1$, then display the maximum length of a non-uniform sequence.
2. If $c=2$, then display the total number of non-uniform sequences in the array.

# Input Data

The file `numere.in` contains on the first line, separated by a space, the natural numbers $n$ and $c$, with the significance described in the statement. The second line contains $n$ natural numbers, separated by a space.

# Output Data

If $c=1$, then on the first line of the file `numere.out` a single number will be written, representing the maximum length of a non-uniform sequence.  
If $c=2$, then the file `numere.out` will contain a single number, which represents the total number of non-uniform sequences.

# Constraints and Clarifications

* $0 < n < 10 \ 000$
* $1 <$ value in the array $< 10 \ 000$
* length of a sequence $\geq 2$

# Example 1

`numere.in`
```
6 1
14 2 49 3 35 1024  
```

`numere.out`
```
5
```

## Explanation

The $6$ numbers are replaced with the values: $7, 2, 7, 3, 7, 2$.  
The length of the longest non-uniform sequence is $5$; the non-uniform sequences of this length are $7, 2, 7, 3, 7$ or $2, 7, 3, 7, 2$.

# Example 2

`numere.in`
```
10 2
14 8 3 25 6 24 20 1024 100 2
```

`numere.out`
```
9
```

## Explanation

The $10$ numbers are replaced with the values: $7, 2, 3, 5, 3, 3, 5, 2, 5, 2$.  
The total number of non-uniform sequences in the array is $3+3+3=9$.