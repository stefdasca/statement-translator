Rules

The tests for this problem are not sufficiently well-constructed to correctly distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! In math class, Gigel learns about sequences. To better understand how they work, he tries to first construct some special sequences based on certain criteria, sequences that have only integer terms. A rule $a$ for a sequence $x$ is an array $(a_1, a_2, \dots, a_K)$. Based on the first element of the sequence, $x_0$, and the array $a$, the sequence $x$ is uniquely determined by the recurrence relation:
$$x_i = x_{i-1} + a_{i \mod K},$$
if $i \mod K$ is not $0$, or
$$x_i = x_{i-1} + a_K,$$
if $i \mod K$ is $0$. By $A \mod B$ we understand the remainder of the division of number $A$ by $B$. Gigel writes down the first $N$ elements of the sequence $x$, $x_0, x_1, \dots, x_{N-1}$, sequence obtained according to the procedure above. Of course, after a while, after Gigel forgets the rule he used to obtain the sequence in the notebook, questions arise. What is the shortest array $a$ (in terms of the number of elements), according to which the first $N$ elements of the sequence $x$ can be obtained?

## Task

## Input data

The input file is `reguli.in`. The first line of this file contains $N$. The next $N$ lines contain one integer each, the value of element $x_{i-1}$ being on line $i+1$.

## Output data

The first line of the file `reguli.out` contains $K$, the minimum length of an array $(a_1, a_2, \dots, a_K)$ that can generate the first $N$ elements of the sequence $x$. The next $K$ lines describe the determined array, the value $a_i$ being on line $i+1$.

## Constraints

$5 \leq N \leq 500\ 000$

The first $N$ numbers of the sequence $x$ are always within signed 64-bit integers.

## Example

`reguli.in`
```
8
8
10
14
13
15
19
18
20
```

`reguli.out`
```
3
2
4
-1
```

## Explanation

The shortest determined rule is $2, 4, -1$. Thus, the elements are obtained as follows:
$$x_1 = x_0 + a_1 = 8 + 2 = 10$$
$$x_2 = x_1 + a_2 = 10 + 4 = 14$$
$$x_3 = x_2 + a_3 = 14 + (-1) = 13$$
$$x_4 = x_3 + a_1 = 13 + 2 = 15$$
$$x_5 = x_4 + a_2 = 15 + 4 = 19$$
$$x_6 = x_5 + a_3 = 19 + (-1) = 18$$
$$x_7 = x_6 + a_1 = 18 + 2 = 20$$