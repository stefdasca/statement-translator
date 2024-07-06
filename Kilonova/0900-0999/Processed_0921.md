```markdown
The force of a non-zero natural number $X$ is equal to the number of positive divisors of $X$. For example, the number $X = 10$ has a force of $4$, because $10$ has $4$ divisors, the set of divisors being $D_{10} = \{1,2,5,10\}$.

Write a program that, given a sequence of $n$ non-zero natural numbers, solves the following tasks:

1. Determine the smallest number in the sequence that has the maximum force;
2. Determine the maximum length of a subarray composed of numbers with the same force that can be obtained by conveniently rearranging the elements of the sequence.

# Input data

The input file `forta.in` contains:

- The first line contains the number $c$ representing the task to be solved ($1$ or $2$).
- The second line contains a natural number $n$.
- The next line contains $n$ natural numbers separated by spaces, representing the elements of the array.

# Output data

The output file `forta.out` will contain a single line that will print a natural number representing the answer to task $c$.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $1 \leq$ the numbers in the array $\leq 2 \cdot 10^9$;
* A subarray consists of one or more numbers located at consecutive positions in the array. The length of a subarray is equal to the number of values that compose it.
* For the first task, $50$ points are awarded, and for the second task, $40$ points are awarded.
* For tests worth $30$ points, $1 \leq n \leq 10\ 000$.

# Example 1

`forta.in`
```
1
6
17 243 10 32 25 13
```

`forta.out`
```
32
```

## Explanation

The task is $1$. $D_{17}=\{1,17\}, D_{243}=\{1,3,9,27,81,243\}, D_{10}=\{1,2,5,10\}, D_{32}=\{1,2,4,8,16,32\}, D_{25}=\{1,5,25\}, D_{13}=\{1,13\}$. Thus, the largest force is $6$, and the smallest number with this force is $32$.

# Example 2

`forta.in`
```
2
8
121 10 14 25 49 9 25 15
```

`forta.out`
```
5
```

## Explanation

The task is $2$. A possible rearrangement of the array could be $(10\ 14\ 15)(121\ 25\ 49\ 9\ 25)$ so that we can obtain a subarray of length $3$ of numbers with force $4$ and a subarray of length $5$ of numbers with force $3$.
```