```markdown
We consider $n$ sets. Each set contains only consecutive natural numbers. To indicate such a set, it is sufficient to provide the first and the last element from it.

# Task

Write a program that determines the elements of the intersection of the $n$ sets.

# Input data

The first line of the input file `multimi.in` contains the number $n$. Then, on each of the next $n$ lines, pairs of numbers are read, one pair per line, separated by a space, representing the smallest and the largest element of each set.

# Output data

The first line of the output file `multimi.out` will contain the intersection elements with a space between them. If the intersection has no elements, the message `multimea vida` will be displayed.

# Constraints and clarifications

* $1 \leq n \leq 30$
* The elements of the sets are natural numbers $\leq 30 \ 000$.

# Example

`multimi.in`
```
3
5 10
4 11
2 9
```

`multimi.out`
```
5 6 7 8 9
```

## Explanation

We have the sets $\{5,6,7,8,9,10\}$, $\{4,5,6,7,8,9,10,11\}$, $\{2,3,4,5,6,7,8,9\}$.

Their intersection is $\{5,6,7,8,9\}$.
```