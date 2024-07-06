### Macarie received a new task in informatics, with the following statement:

Consider a sequence of non-zero natural numbers, $A$ with $N$ elements. Let the increasing sequence $D$ be formed from all natural divisors, not necessarily distinct, of the elements in $A$. For example, for $N=4$ and $A=(6, 2, 3, 2)$, we have the sequence $D=(1,1,1,1,2,2,2,3,3,6)$.

# Task

Given a sequence $Poz$ consisting of $Q$ non-zero natural numbers, representing positions in sequence $D$, determine the corresponding element from sequence $D$ for each of them.

# Input data

The first line of the input file `macarie.in` contains the natural numbers $N$ and $Q$.  
The second line contains $N$ non-zero natural numbers, representing, in order, the terms of sequence $A$.  
The third line contains $Q$ non-zero natural numbers, representing, in order, the elements of sequence $Poz$. Numbers on the same line of the input file are separated by a single space.

# Output data

The first line of the output file `macarie.out` contains $Q$ non-zero natural numbers, separated by a single space, representing elements from $D$, in the order their positions appear in sequence $Poz$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$, $1 \leq Q \leq 100 \ 000$;
* The numbering of elements within sequences $A$, $D$ and $Poz$ starts from $1$.
* $1 \leq A_i \leq 1 \ 000 \ 000$ for $1 \leq i \leq N$. The terms of sequence $A$ are not necessarily distinct.
* $1 \leq Poz_i \leq |D|$ for $1 \leq i \leq Q$, where $|D|$ is the length of sequence $D$.

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 23 | All values in the input file are $\leq 1 \ 000$ |
| 2 | 18 | All values $A_i$ are prime numbers |
| 3 | 23 | $N \leq 10 \ 000$, $Poz_i \leq 2 \ 000 \ 000$ |
| 4 | 15 | $Poz_i \leq 2 \ 000 \ 000$ |
| 5 | 21 | No additional constraints |

# Example 1

`macarie.in`
```
4 5 
32 42 49 21
2 5 9 7 17
```

`macarie.out`
```
1 2 4 3 21
```

## Explanation

$N = 4$ and $Q = 5$. $A = (32, 42, 49, 21)$ and $D = (1, \underline{1}, 1, 1, \underline{2}, 2, \underline{3}, 3, \underline{4}, 6, 7, 7, 7, 8, 14, 16, \underline{21}, 21, 32, 42, 49)$.

# Example 2

`macarie.in`
```
5 4
24 56 8 490 28
35 25 28 38
```

`macarie.out`
```
70 12 14 490
```

## Explanation

$N = 5$, $Q = 4$ and $D[35] = 70$, $D[25] = 12$, $D[28] = 14$, $D[38] = 490$.
