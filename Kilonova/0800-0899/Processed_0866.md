Maria has $N$ beads placed next to each other in her room. On each of them, a natural number formed of distinct nonzero digits is written. For each bead, Maria erases the number and writes another in its place, containing only two digits, specifically the smallest and largest digits from the initially written number, in the order they appeared before erasing. Now, Maria considers that the beads are of two types, based on the two-digit number written on them: type $1$ (those with the tens digit smaller than the units digit) and type $2$ (the others). Using the beads, the girl wants to obtain, by removing some of them (without changing the order of the others), a **circular** necklace as long as possible that respects the property that any two neighboring beads are of different types. In the necklace formed with the remaining beads after removal, the first bead is considered neighboring with the last one.

# Task

1. Determine the number of type $1$ beads.
2. Determine the maximum number of beads the necklace can have.

# Input data

The input file `colier.in` contains on the first line a natural number $T$. The second line contains a natural number $N$. The third line contains $N$ natural numbers, representing, in order, the initial values written on the beads. These numbers are separated by a space.

# Output data

If the value of $T$ is 1, only point (1) from the task will be solved. In this case, the output file `colier.out` will contain on the first line a natural number representing the answer to task (1).

If the value of $T$ is 2, only point (2) from the task will be solved. In this case, the output file `colier.out` will contain on the first line a natural number representing the answer to task (2).

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$;
* The numbers initially written on the beads have distinct digits, do not contain the digit $0$ and are between $12$ and $987\ 654\ 321$;
* $T$ will be $1$ or $2$;
* For obtaining the necklace, Maria can decide not to remove any bead;
* The obtained necklace can be formed of a single bead;
* For tests worth $20$ points, $T = 1$ and all the numbers initially written on the beads have two digits;
* For tests worth $30$ points, $T = 1$ and among the numbers initially written on the beads, there are some with more than two digits;
* For tests worth $50$ points, $T = 2$.

# Example 1

`colier.in`
```
1
5
12 678 312 24 938
```

`colier.out`
```
3
```

## Explanation

The numbers written by Maria on the beads will be, in order: $12$, $68$, $31$, $24$, $93$. Three of them ($12$, $68$ and $24$) are of type $1$. ($T$ being $1$, only task $1$ is solved).

# Example 2

`colier.in`
```
2
5
12 678 312 24 938
```

`colier.out`
```
4
```

## Explanation

The numbers written by Maria on the beads will be, in order: $12$, $68$, $31$, $24$, $93$. By removing the bead at position $1$ or the one at position $2$ and arranging the others circularly, we obtain a necklace with $4$ beads in which any two neighbors are of different types. ($T$ being $2$, only task $2$ is solved).

Maria is forced to remove one of the two beads; otherwise, there would be neighboring beads of the same type.