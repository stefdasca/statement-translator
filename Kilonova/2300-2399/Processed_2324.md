
To enter the Record Book, the inhabitants of Văscăuți will make a very very long string of beads. For this purpose, they bought beads of $K$ colors (for each color $i$, the number $a_i$ of beads bought is known).
The inhabitants of Văscăuți consider the string to be beautiful if any subarray of $P$ consecutive beads in the string $(2 \leq P \leq K)$ does not contain two beads of the same color.

# Task

Write a program that determines the maximum length of a beautiful string that can be constructed with the beads bought.

# Input data

The input file `sirag.in` contains on the first line the natural numbers $K$ and $P$ separated by space. The next $K$ lines contain in order the values $a_1, a_2, \dots , a_K$, each value on one line.

# Output data

The output file `sirag.out` will contain a single line that will contain the natural number $L_{Max}$, representing the maximum length of a beautiful string that can be constructed with the beads bought.

# Constraints and clarifications

* $2 \leq P \leq K \leq 100\ 000$;
* $1 \leq a_i \leq 10^9$;

# Example

`sirag.in`
```
4 3
2
5
2
1
```

`sirag.out`
```
8
```

## Explanation

A beautiful string of maximum length $8$ is $2, 4, 3, 1, 2, 3, 1, 2$
