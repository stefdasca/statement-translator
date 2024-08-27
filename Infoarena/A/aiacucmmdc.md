# Aiacucmmdc

Not knowing what story to come up with for this problem, the author decided not to complicate the contestants with unnecessary texts, which can be more confusing when reading the task. Thus, a sequence of $N$ natural numbers is given. The task is to determine the number of subarrays of the sequence, with the property that the GCD of the subarray is divisible by a natural number $P$. Super simple. By subarray, we mean a sequence of one or more elements located at consecutive positions in the initial sequence.

## Task

## Input data

The input file `aiacucmmdc.in` contains on the first line a natural number $N$ (representing the number of elements in the sequence) and the natural number $P$. On the next line, there are $N$ natural numbers separated by space, representing the elements of the sequence.

## Output data

The output file `aiacucmmdc.out` will contain on the first line a natural number $K$, representing the number of subarrays with the required property.

## Constraints and clarifications

The GCD (greatest common divisor) is understood as the greatest common divisor of the respective numbers. By definition, the greatest common divisor of a single number is the number itself.
$1 \leq N \leq 1\ 000\ 000$

$1 \leq a[i], P \leq 2\ 000\ 000\ 000$

For tests worth 10 points $N \leq 250$

For tests worth 25 points $N \leq 3\ 000$

For tests worth 50 points $N \leq 10\ 000$ and the number of subarrays will not exceed $1\ 500\ 000$

For tests worth 90 points $N \leq 1\ 000\ 000$

Examples will represent tests worth 10 ("points by default") and will have feedback.

## Example

`aiacucmmdc.in`
```
6 3 
2 9 6 4 3 13 
```

`aiacucmmdc.out`
```
4 
```

## Explanation

$N = 6$, $P = 3$

The 4 subarrays are:

from 2 to 2 = $\{9\}$ with GCD = $9$

from 3 to 3 = $\{6\}$ with GCD = $6$

from 2 to 3 = $\{9, 6\}$ with GCD = $3$

from 5 to 5 = $\{3\}$ with GCD = $3$