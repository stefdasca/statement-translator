# Task

Every natural number greater than $2$ can be written as a sum of non-zero natural numbers **in strictly ascending order**, such that each term of the sum, except for the first term, is a multiple of the previous term in the sum. For example, $27=3+6+18$, where $6$ is a multiple of $3$ and $18$ is a multiple of $6$. Since we desire a decomposition with as many terms as possible, we can also obtain decompositions with $4$ terms: $27=1+2+8+16$ or $27=1+2+4+20$ or $27=1+2+6+18$. Among the three decompositions with $4$ terms, the decomposition $27=1+2+4+20$ is minimal from a lexicographic point of view ($1$ and $2$ are the same in all 3 decompositions, but $4<6$ and $4<8$). The number $30$ can be decomposed as $30=2+4+8+16$. It also has a decomposition of length $4$, but it is larger in lexicographic terms than any of the decompositions with $4$ terms of $27$ ($2 > 1$).

# Task

For multiple data sets consisting of two natural numbers $A$ and $B$, $A \leq B$, it is required to determine, for each set, one of the following tasks:
$1)$ the maximum number of terms in which the numbers in the interval $[A, B]$ can be decomposed according to the rule described in the statement;
$2)$ the number of numbers in the interval $[A, B]$ that can be decomposed with a maximum number of terms;
$3)$ the number in the interval $[A, B]$ that admits a decomposition with a maximum number of terms, minimal from a lexicographic point of view.

# Input data

From the file `multisum.in`, read on the first line, two numbers $N$ and $C$, separated by a space, representing the number of data sets and the type of task: $C=1$ for task $1$, $C=2$ for task $2$ and $C=3$ for task $3$. From the following $N$ lines of the file, read each pair of numbers $A$ and $B$, separated by a space.

# Output data

In the file `multisum.out`, write one line for each pair $A, B$ from the input file. Each line will contain the required number, according to the task: if $C=1$, the number will represent the maximum number of terms in a decomposition; if $C=2$, the number will represent the number of values in the respective interval that can be decomposed with a maximum number of terms; and if $C=3$, the number will represent that value in the respective interval that admits a decomposition with a maximum number of terms, minimal from a lexicographic point of view.

# Constraints and clarifications

* $0 < N \leq 1\ 000$;
* $2 < A \leq B \leq 100\ 000$;
* The sum of the lengths of the intervals in all sets of a test will not exceed $100\ 000$;
* For a correct solution to task $1$, $20\%$ of the score is awarded, for task $2$ $40\%$ of the score is awarded, and for task $3$ $40\%$ of the score is awarded;
* For tests worth $30$ points, $N \leq 50, B \leq 1\ 000$ and the sum of the lengths of the intervals in the tests will not exceed $10\ 000$.

# Example 1

`multisum.in`
```
1 1
50 60
```

`multisum.out`
```
5
```

## Explanation

There is only one set of data. Task $1$ is solved.

The maximal decompositions of the numbers in the interval have some $4$ terms, others $5$ terms. So the highest number of terms is $5$ (and this is obtained for the numbers $55$, $57$, $58$, and $59$).

# Example 2

`multisum.in`
```
1 2
50 60
```

`multisum.out`
```
4
```

## Explanation

There is only one set of data. Task $2$ is solved.

The numbers that can be decomposed into a maximum number of terms are $55$, $57$, $58$, and $59$. So there are $4$ numbers that admit a maximal decomposition.

# Example 3

`multisum.in`
```
1 3
50 60
```

`multisum.out`
```
55
```

## Explanation

There is only one set of data. Task $3$ is solved.

The $4$ numbers that admit maximal decompositions are:
- $55=1+2+4+16+32$;
- $55=1+2+4+12+36$;
- $55=1+2+4+8+40$;
- $57=1+2+6+12+36$;
- $58=1+3+6+12+36$;
- $59=1+2+8+16+32$.

The smallest sum from a lexicographic point of view is $1+2+4+8+40$ and it corresponds to the number $55$.

# Example 4

`multisum.in`
```
3 3
50 50
10 13
16 17
```

`multisum.out`
```
50
11
17
```

## Explanation

There are $3$ sets of data. Task $3$ is solved.

- The interval $[50, 50]$ contains only the number $50$ which admits a single maximal decomposition (with $4$ terms) and this is minimal from a lexicographic point of view.
- Among the numbers in the interval $[10,13]$, the numbers $10$, $11$, and $13$ admit a decomposition with a maximum number of terms ($3$ terms), but a maximal decomposition of $11$ ($1+2+8$) is minimal from a lexicographic point of view.
- In the interval $[16,17]$ the numbers admit two maximal decompositions:
    - $16=1+3+12$;
    - $16=1+5+10$;
    - $17=1+2+14$;
    - $17=1+4+12$.
    The minimal decomposition from a lexicographic point of view is $1+2+14$ and corresponds to the value $17$.