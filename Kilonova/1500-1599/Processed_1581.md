```markdown
We consider an array with $N$ integer elements. We define the following notions:

* **sequence in the array** = elements positioned consecutively in the array
* **length of a sequence** = the number of elements that make it up
* **sum of a sequence** = the sum of the elements that make it up
* **non-trivial sequence** = sequence of length at least $2$
* **N-sequence** = sequence whose sum is divisible by $N$ (the sequence can also be trivial)
* **non-trivial N-sequence** = non-trivial sequence whose sum is divisible by $N$.

# Task

Write a program that reads the natural number $N$ and then the array of $N$ elements. The program should determine:

1. the number of non-trivial $N$-sequences from the array;
2. the largest length of an $N$-sequence from the array;
3. the largest sum of an $N$-sequence from the array.

# Input data

The input file `secvente.in` contains on the first line the natural numbers $C$ and $N$, separated by a single space. $C$ represents the task to be solved ($1, 2$, or $3$).

# Output data

The file `secvente.out` will contain on the first line a natural number representing:

if $C = 1$, the number of non-trivial **N-sequences** from the array (the answer for task $1$);

if $C = 2$, the largest length of an **N-sequence** from the array (the answer for task $2$);

if $C = 3$, the largest sum of an **N-sequence** from the array (the answer for task $3$).

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* The elements of the array are integers in the closed interval $[-10^9, 10^9]$
* In the given array, there exists at least one **N-sequence** whose sum is a natural number.
* The negative integer $X$ is divisible by the nonzero natural number $N$ if the remainder of dividing the absolute value of $X$ by $N$ is $0$ (for example, $X=-30$ is divisible by $N=6$, and $X=-45$ is not divisible by $N=6$).
* For each of tasks $1$ and $2$ there are $30$p, and for task $3$ there are $40$p.

# Example 1

`secvente.in`
```
1 10
-9 -3 4 -10 -1 -16 18 18 -10 50
```

`secvente.out`
```
8
```

## Explanation

We solve task $1$. The array has $N=10$ integer elements: $-9, -3, 4, -10, -1, -16, 18, 18, -10, 50$.

The **non-trivial N-sequences** are ($-3, 4$ , $-10, -1$), ($-16, 18, 18$), ($-10, 50$), ($-16, 18$ , $18, -10$), ($-16, 18$ , $18, -10, 50$), ($-3, 4, -10$ , $-1, -16, 18, 18$), ($-3, 4, -10$ , $-1, -16, 18$ , $18, -10$), ($-3, 4, -10$ , $-1, -16, 18$ , $18, -10, 50$).

# Example 2

`secvente.in`
```
2 10
-9 -3 4 -10 -1 -16 18 18 -10 50
```

`secvente.out`
```
9
```

## Explanation

We solve task $2$. The array has $N=10$ integer elements: $-9, -3, 4, -10$ , $-1, -16, 18$ , $18, -10, 50$.

The longest of these sequences is the **N-sequence** ($-3, 4, -10, -1$ , $-16, 18, 18$ , $-10, 50$). The length of this sequence is $9$.

# Example 3

`secvente.in`
```
3 10
-9 -3 4 -10 -1 -16 18 18 -10 50
```

`secvente.out`
```
60
```

## Explanation

We solve task $3$. The array has $N=10$ integer elements: $-9, -3, 4, -10$ , $-1, -16, 18$ , $18, -10, 50$.

The maximum sum of a sequence is $60$ (the sum of the **N-sequence**: $-16, 18, 18$ , $-10, 50$).
```