The FMI NO STRESS committee has been very diligent in preparing the contest. Each member of the committee has tallied the number of hours spent working on each problem and then marked it in a matrix with $N$ rows and $M$ columns, where the element in row $i$ and column $j$ represents the number of hours member $i$ spent working on problem $j$.

# Task

The committee wishes to know who was the least ~~lazy~~ working member, and also the most diligent. Since they are exhausted, they ask you to calculate this information.

# Input data

The first line contains two natural numbers, $N$ and $M$, representing the dimensions of the matrix. Each of the following $N$ lines contains $M$ natural numbers, representing the matrix.

# Output data

The first line will contain two natural numbers, representing the index of the least ~~lazy~~ working member, and the index of the most diligent member. If two or more members share the position of the least ~~lazy~~ working member, the smaller index is displayed. The same applies for the most diligent ones.

# Constraints and clarifications

* $1 \leq N, M \leq 100$;
* The elements of the matrix are natural numbers (the committee did not want to calculate to the millisecond; an approximation is sufficient) within the range $[0, 100]$.

# Example

`stdin`
```
3 3
1 2 3
4 5 6
7 8 9
```

`stdout`
```
1 3
```

## Explanation

The first member worked a total of $6$ hours, the second member a total of $15$ hours, and the third a total of $24$ hours. The first member worked the least, while the third worked the most.