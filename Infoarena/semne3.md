## Task

Professor Onizuka has $N$ students in his class. They are numbered from $1$ to $N$. He received a sheet with $N - 1$ signs of the type: $<$ and $>$. He needs to arrange the $N$ students in desks (the desks being arranged in a line), so that the student indices correspond to the imposed signs (if the first sign is $>$, then the student in desk $1$ must have an index greater than the student in desk $2$).

## Input data

The input file `semne3.in` will contain on the first line a natural number $N$. The second line will contain $N - 1$ signs of the type $<$ and $>$.

## Output data

The output file `semne3.out` will contain $N$ numbers representing the indices of the students placed in the $N$ desks (the $i$-th number will contain the index of the student placed in desk $i$). The minimal lexicographic solution is required.

## Constraints and clarifications

$1 \leq N \leq 500\ 000$

For $70\%$ of the points, any solution can be displayed (not necessarily the minimal lexicographic one).

## Example

`semne3.in`

```
4
><>
```

`semne3.out`

```
2 1 4 3
```

## Explanation

$2 > 1 < 4 > 3$

